import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# Function to handle topic selection
def select_topic():
    selected_topic = topic_listbox.get(tk.ACTIVE)
    messagebox.showinfo("Topic Selected", f"Topic selected: {selected_topic}")

# Function to handle search
def search_topics():
    search_query = search_entry.get()
    # Perform search logic here
    messagebox.showinfo("Search", f"Searching for: {search_query}")

# Create the main window
root = tk.Tk()
root.title("IoT Security App")
root.geometry("800x600")

# Create a frame for the welcome screen
welcome_frame = ttk.Frame(root)
welcome_frame.pack(pady=20)

# Create the settings icon
settings_icon = tk.PhotoImage(file="settings_icon.png")
settings_button = ttk.Button(welcome_frame, image=settings_icon, style="Toolbutton")
settings_button.grid(row=0, column=0, sticky="e")

# Create the welcome label
welcome_label = ttk.Label(welcome_frame, text="Welcome to IoT Security App!", font=("Helvetica", 18))
welcome_label.grid(row=1, column=0, padx=20, pady=10)

# Create a frame for the topic page
topic_frame = ttk.Frame(root)

# Create the search entry and button
search_entry = ttk.Entry(topic_frame, width=40)
search_entry.grid(row=0, column=0, padx=10, pady=10)
search_button = ttk.Button(topic_frame, text="Search", command=search_topics)
search_button.grid(row=0, column=1, padx=10)

# Create the topic listbox
topic_listbox = tk.Listbox(topic_frame, width=50, height=15)
topic_listbox.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

# Add topics to the listbox
topics = ["Asset Protection", "Third-Party Management", "Operation and Maintenance", "Monitoring and Incident Management"]
for topic in topics:
    topic_listbox.insert(tk.END, topic)

# Create the topic description label
description_label = ttk.Label(topic_frame, text="Select a topic to view its description", font=("Helvetica", 12))
description_label.grid(row=2, column=0, columnspan=2, padx=10, pady=5)

# Create the topic description text widget
description_text = tk.Text(topic_frame, width=60, height=10, wrap=tk.WORD)
description_text.grid(row=3, column=0, columnspan=2, padx=10, pady=5)

# Create the topic selection button
select_button = ttk.Button(topic_frame, text="Select", command=select_topic)
select_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

# Switch to the welcome frame initially
topic_frame.pack_forget()
welcome_frame.pack()

# Function to switch to the topic frame
def show_topic_frame():
    welcome_frame.pack_forget()
    topic_frame.pack()

# Function to switch to the welcome frame
def show_welcome_frame():
    topic_frame.pack_forget()
    welcome_frame.pack()

# Bind the settings button to switch frames
settings_button.configure(command=show_topic_frame)

# Create a go back button
go_back_button = ttk.Button(topic_frame, text="Go Back", command=show_welcome_frame)
go_back_button.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()
