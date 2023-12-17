#bot.py with GUI
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer


chatbot = ChatBot("Chatbot")

trainer = LisatTrainer(chatbot)
trainer.train([
	"Salut"
	"Buna ziua. cum va pot ajuta? 🤗"
])
trainer.train([
	"Vreau sa vorbesc/contactez o persoana fizica"
	"Pentru a contacta un asistent uman va rog sa sunati la numarul de telefon NR_TEL intre orele 9AM-5PM" 
while True:
	query = input("Asistent: ")
	if query in exit_conditions:
		break
	else:
		print(f"{chatbot.get_response(query)}")
