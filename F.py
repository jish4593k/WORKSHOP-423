import fitz  
import torch
import tkinter as tk
from tkinter import scrolledtext, ttk
import seaborn as sns
import matplotlib.pyplot as plt
from PIL import Image, ImageTk



def visualize_tensor(tensor_data):
    sns.set(style="whitegrid")

 
    plt.figure(figsize=(10, 6))
    sns.barplot(x=list(range(len(tensor_data))), y=tensor_data)

    plt.title("Tensor Data Visualization")
    plt.xlabel("Index")
    plt.ylabel("Value")
    plt.show()

class PDFTextExtractorApp:
    def __init__(self, master):
        self.master = master
        self.master.title("PDF Text Extractor")

        
        self.pdf_path_label = ttk.Label(master, text="Enter PDF File Path:")
        self.pdf_path_label.pack(pady=10)

        self.pdf_path_entry = ttk.Entry(master)
        self.pdf_path_entry.pack(pady=10)

        self.extract_button = ttk.Button(master, text="Extract Text", command=self.extract_and_display_text)
        self.extract_button.pack(pady=20)

        self.text_display = scrolledtext.ScrolledText(master, width=80, height=20)
        self.text_display.pack(pady=10)

    def extract_and_display_text(self):
        pdf_path = self.pdf_path_entry.get()
        try:
            extracted_text = ""
            for page_text in extract_text_by_page(pdf_path):
                extracted_text += page_text + "\n"

            self.text_display.delete(1.0, tk.END)
            self.text_display.insert(tk.END, extracted_text)

          
            tensor_data = [len(page_text) for page_text in extract_text_by_page(pdf_path)]
            visualize_tensor(tensor_data)
        except Exception as e:
            self.text_display.delete(1.0, tk.END)
            self.text_display.insert(tk.END, f"An error occurred: {str(e)}")

def main():
    root = tk.Tk()
    app = PDFTextExtractorApp(root)
    root.mainloop()

if __name__ == '__main__':
    main()

