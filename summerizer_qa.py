# James Griffin Gomez
## PDF Summarization and QA + interactive text chunks to help my brother study for his med school finals! 

#Import Block 
#from transformers import pipeline
import streamlit as st 
import os 
import tempfile
#lang chain libraries
from langchain.document_loaders import PyPDFLoader
from langchain import PromptTemplate
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains.summarize import load_summarize_chain
from langchain.chat_models import ChatOpenAI