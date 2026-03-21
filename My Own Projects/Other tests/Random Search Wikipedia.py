import tkinter as tk
import requests
from bs4 import BeautifulSoup

def get_random_wikipedia_article():
    response = requests.get("https://en.wikipedia.org/wiki/Special:Random")
    soup = BeautifulSoup(response.content, "html.parser")
    title = soup.find(id="firstHeading").text
    paragraphs = soup.find_all('p')
    content = '\n'.join([para.text for para in paragraphs if para.text.strip() != ''])
    url = response.url
    return title, content, url

def display_article():
    title, content, url = get_random_wikipedia_article()
    title_label.config(text=url)
    text_widget.delete(1.0, tk.END)
    text_widget.insert(tk.END, content)

root = tk.Tk()
root.title("Random Wikipedia Article")

title_label = tk.Label(root, text="", font=("Helvetica", 16, "bold"), wraplength=600)
title_label.pack(pady=10)

text_widget = tk.Text(root, wrap=tk.WORD, width=80, height=20)
text_widget.pack(pady=10)

refresh_button = tk.Button(root, text="Get Random Article", command=display_article)
refresh_button.pack(pady=10)

display_article()

root.mainloop()