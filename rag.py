from langchain_community.chat_models import ChatOllama
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.vectorstores import Chroma
from langchain.schema.output_parser import StrOutputParser
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_core.runnables import RunnableParallel, RunnablePassthrough
from langchain.prompts import PromptTemplate
from langchain.vectorstores.utils import filter_complex_metadata
from langchain.globals import set_verbose, set_debug

set_verbose(True)
set_debug(True)

class ChatPDF:
    vector_store = None
    retriever = None
    chain = None


    def __init__(self):
        self.model = ChatOllama(model="mistral")
        self.text_splitter = RecursiveCharacterTextSplitter(chunk_size=512, chunk_overlap=100)
        self.prompt = PromptTemplate.from_template(
            """
            <s>[INST]<<SYS>> Sei un assistente virtuale che risponde alle domande degli utenti. Se presente un Contesto, utilizzalo per rispondere alla domanda. Usa tre frasi
             massimo e mantieni la risposta concisa.<</SYS>>
             Domanda: {question}
             Contesto: {context}
             Risposta: [/INST]
            """
        )

    def ingest(self, pdf_file_path: str):
        docs = PyPDFLoader(file_path=pdf_file_path).load()
        chunks = self.text_splitter.split_documents(docs)
        chunks = filter_complex_metadata(chunks)

        vector_store = Chroma.from_documents(documents=chunks, embedding=OllamaEmbeddings(model="nomic-embed-text"))
        self.retriever = vector_store.as_retriever(
            search_type="mmr"
        )


        def format_docs(docs):
            return "\n\n".join(doc.page_content for doc in docs)
        

        self.chain = (
            {"context": self.retriever | format_docs, "question": RunnablePassthrough()}
            | self.prompt
            | self.model
            | StrOutputParser()
        )

    def ask(self, query: str):
        if not self.chain:
            return "Please, add a PDF document first."

        return self.chain.stream(query)

    def clear(self):
        self.vector_store = None
        self.retriever = None
        self.chain = None
