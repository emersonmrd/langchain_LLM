from langserve import RemoteRunnable

chain_remota = RemoteRunnable("http://localhost:8000/translator/")
texto = chain_remota.invoke({"idioma": "espanhol", "texto": "Texto de exemplo"})
print(texto)
