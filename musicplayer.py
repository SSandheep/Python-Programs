{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "66010b8e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: pygame in c:\\users\\shubh\\anaconda3\\lib\\site-packages (2.5.0)\n"
     ]
    }
   ],
   "source": [
    "!pip install pygame"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3e89ad92",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "pygame 2.5.0 (SDL 2.28.0, Python 3.9.13)\n",
      "Hello from the pygame community. https://www.pygame.org/contribute.html\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "Exception in Tkinter callback\n",
      "Traceback (most recent call last):\n",
      "  File \"C:\\Users\\shubh\\anaconda3\\lib\\tkinter\\__init__.py\", line 1892, in __call__\n",
      "    return self.func(*args)\n",
      "  File \"C:\\Users\\shubh\\AppData\\Local\\Temp\\ipykernel_16456\\2595095683.py\", line 23, in set_volume\n",
      "    pygame.mixer.music.set_volume(volume)\n",
      "TypeError: must be real number, not str\n"
     ]
    }
   ],
   "source": [
    "import tkinter as tk\n",
    "import pygame\n",
    "from tkinter import filedialog\n",
    "\n",
    "def play_music():\n",
    "    try:\n",
    "        file_path = file_path_entry.get()\n",
    "        pygame.mixer.music.load(file_path)\n",
    "        pygame.mixer.music.play()\n",
    "    except pygame.error as e:\n",
    "        print(\"Error occurred while playing the music:\", str(e))\n",
    "\n",
    "def pause_music():\n",
    "    pygame.mixer.music.pause()\n",
    "\n",
    "def resume_music():\n",
    "    pygame.mixer.music.unpause()\n",
    "\n",
    "def stop_music():\n",
    "    pygame.mixer.music.stop()\n",
    "\n",
    "def set_volume(volume):\n",
    "    pygame.mixer.music.set_volume(volume)\n",
    "\n",
    "def browse_file():\n",
    "    file_path = filedialog.askopenfilename(filetypes=((\"Audio files\", \"*.mp3\"), (\"All files\", \"*.*\")))\n",
    "    file_path_entry.delete(0, tk.END)\n",
    "    file_path_entry.insert(tk.END, file_path)\n",
    "\n",
    "# Initialize pygame mixer\n",
    "pygame.mixer.init()\n",
    "\n",
    "# Create the main window\n",
    "window = tk.Tk()\n",
    "window.title(\"Music Player\")\n",
    "\n",
    "# Create the file path entry\n",
    "file_path_entry = tk.Entry(window, width=50)\n",
    "file_path_entry.pack()\n",
    "\n",
    "# Create the browse button\n",
    "browse_button = tk.Button(window, text=\"Browse\", command=browse_file, width=10, height=2)\n",
    "browse_button.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)\n",
    "\n",
    "# Create the play button\n",
    "play_button = tk.Button(window, text=\"Play\", command=play_music, width=10, height=2)\n",
    "play_button.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)\n",
    "\n",
    "# Create the pause button\n",
    "pause_button = tk.Button(window, text=\"Pause\", command=pause_music, width=10, height=2)\n",
    "pause_button.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)\n",
    "\n",
    "# Create the resume button\n",
    "resume_button = tk.Button(window, text=\"Resume\", command=resume_music, width=10, height=2)\n",
    "resume_button.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)\n",
    "\n",
    "# Create the stop button\n",
    "stop_button = tk.Button(window, text=\"Stop\", command=stop_music, width=10, height=2)\n",
    "stop_button.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)\n",
    "\n",
    "# Create the volume scale\n",
    "volume_label = tk.Label(window, text=\"Volume\")\n",
    "volume_label.pack()\n",
    "\n",
    "volume_scale = tk.Scale(window, from_=0, to=1, resolution=0.1, orient=tk.HORIZONTAL, command=set_volume)\n",
    "volume_scale.set(0.5)\n",
    "volume_scale.pack()\n",
    "\n",
    "# Run the GUI main loop\n",
    "window.mainloop()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "348a7c7f",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}