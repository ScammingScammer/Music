import os
import pygame
import keyboard
import time
import pygetwindow

def is_terminal_or_vscode_focused():
    active_window_title = pygetwindow.getActiveWindowTitle()
    terminal_titles = ["Command Prompt", "cmd.exe", "Terminal", "gnome-terminal", "xterm"]
    vscode_title = "Visual Studio Code"
    return any(title in active_window_title for title in terminal_titles) or vscode_title in active_window_title

def play_music_in_order(directory, order=None, loop=True):
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.set_endevent(pygame.USEREVENT)  # Set event for end of music

    # List all files in the directory
    files = [f for f in os.listdir(directory) if f.endswith('.mp3')]

    # Sort the files based on order if provided
    if order:
        files.sort(key=lambda x: order.index(x) if x in order else len(order))

    # Load and play the first file
    current_file = os.path.join(directory, files[0])
    pygame.mixer.music.load(current_file)
    pygame.mixer.music.play()
    os.system('cls')
    print("Loop 1 - Now playing: Position 1 /", len(files), "-", files[0])  # Print out the currently playing file and loop number
    current_index = 0
    loop_count = 1
    playing = True
    paused = False
    last_pressed_time = 0
    delay = 0.5  # Adjust the delay time as needed

    while playing:
        for event in pygame.event.get():
            if event.type == pygame.USEREVENT:
                current_index = (current_index + 1) % len(files)
                current_file = os.path.join(directory, files[current_index])
                pygame.mixer.music.load(current_file)
                pygame.mixer.music.play()
                if current_index == 0:  # If it's the first song
                    loop_count += 1
                os.system('cls')
                print("Loop", loop_count, "- Now playing: Position", current_index + 1, "/", len(files), "-", files[current_index])  # Print out the loop number and currently playing file
            elif event.type == pygame.QUIT:
                playing = False
        
        # Check for key press to pause/unpause if terminal or vscode is focused
        if is_terminal_or_vscode_focused() and keyboard.is_pressed('p') and time.time() - last_pressed_time > delay:
            if not paused:
                pygame.mixer.music.pause()
                print("Music paused")
                paused = True
            else:
                pygame.mixer.music.unpause()
                print("Music resumed")
                paused = False
            last_pressed_time = time.time()
        
        # Check for key press to switch to the next song if terminal or vscode is focused
        if is_terminal_or_vscode_focused() and keyboard.is_pressed('n') and time.time() - last_pressed_time > delay:
            current_index = (current_index + 1) % len(files)
            current_file = os.path.join(directory, files[current_index])
            pygame.mixer.music.load(current_file)
            pygame.mixer.music.play()
            if current_index == 0:  # If it's the first song
                loop_count += 1
            os.system('cls')
            print("Loop", loop_count, "- Now playing: Position", current_index + 1, "/", len(files), "-", files[current_index])  # Print out the loop number and currently playing file
            last_pressed_time = time.time()

        # Check for key press to switch to the previous song if terminal or vscode is focused
        if is_terminal_or_vscode_focused() and keyboard.is_pressed('b') and time.time() - last_pressed_time > delay:
            current_index = (current_index - 1) % len(files)
            if current_index == len(files) - 1:  # If it's the last song
                loop_count -= 1
                if loop_count < 0:
                    loop_count = 0
            current_file = os.path.join(directory, files[current_index])
            pygame.mixer.music.load(current_file)
            pygame.mixer.music.play()
            os.system('cls')
            print("Loop", loop_count, "- Now playing: Position", current_index + 1, "/", len(files), "-", files[current_index])  # Print out the loop number and currently playing file
            last_pressed_time = time.time()

# Example usage:
if __name__ == "__main__":
    directory = "C:\\Users\\Gaming\\Desktop\\Songs I sleep to\\"  # Change this to your directory containing MP3 files
    order = ["MASHLE MAGIC AND MUSCLES The Divine Visionary Candidate Exam Arc  OPENING THEME - 128.mp3",
            "Attack on Titan Season 2 - Opening  Shinzou wo Sasageyo! - 128.mp3",
            "One Piece OST Overtaken - 128.mp3",
            "One Punch Man - Official Opening - The Hero!! Set Fire to the Furious Fist - 128.mp3",
            "One Piece OP 1 - We Are! Lyrics - 128.mp3",
            "One Piece OST OVERTAKEN「Drums of Liberation Music」 EPIC VERSION - 128.mp3",
            "『チェンソーマン』ノンクレジットオープニング  CHAINSAW MAN  Opening│米津玄師 「KICK BACK」 - 128.mp3",
            "JoJo's Bizarre Adventure Golden Wind OST - Giorno's Theme『il vento d'oro』 - 128.mp3"]  # Change this to the order you want
    play_music_in_order(directory, order)