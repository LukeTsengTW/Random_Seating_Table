import pygame, random
import tkinter as tk
from tkinter import filedialog

"""
Random_Seating_Table Ver 1.1
Author : LukeTseng
Release Date : 2024/06/22
Programming Language : Python
"""

pygame.init()

seat_width, seat_height, seat_margin = 50, 50, 10
colors = {'seat_color': (139, 69, 19), 'podium_color': (255, 255, 255), 'text_color': (255, 255, 255), 'podium_text_color': (10, 10, 10), 'button_color': (0, 128, 0), 'button_text_color': (255, 255, 255)}
screen_size = ((seat_width + seat_margin) * 7, (seat_height + seat_margin) * 7 + 60)

# Adjust here to change the number of seats
seats = [(i, j) for i in range(7) for j in range(6) if not (i, j) in [(0, 0), (0, 5), (6, 0), (3, 5), (6, 5)]]
random.shuffle(seats)

window = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Random_Seating_Table")

def draw_seats():
    font = pygame.font.Font(None, 36)
    for i, (x, y) in enumerate(seats):
        pygame.draw.rect(window, colors['seat_color'], [(seat_margin + seat_width) * x + seat_margin, (seat_margin + seat_height) * y + seat_margin, seat_width, seat_height])
        text = font.render(str(i+1), True, colors['text_color'])
        textpos = text.get_rect(centerx=(seat_margin + seat_width) * x + seat_margin + seat_width/2, centery=(seat_margin + seat_height) * y + seat_margin + seat_height/2)
        window.blit(text, textpos)

def draw_podium():
    font = pygame.font.Font(None, 36)
    text = font.render('Podium', True, colors['podium_text_color'])
    podium_rect = [seat_margin, (seat_height + seat_margin) * 7 - seat_margin - seat_height, (seat_width + seat_margin) * 7 - 2 * seat_margin, seat_height]
    pygame.draw.rect(window, colors['podium_color'], podium_rect)
    textpos = text.get_rect(center=(((seat_width + seat_margin) * 7) / 2, podium_rect[1] + seat_height / 2))
    window.blit(text, textpos)

def draw_buttons():
    font = pygame.font.Font('medium_black.ttc', 36)
    screenshot_button_rect = pygame.Rect((screen_size[0] // 2 - 160, screen_size[1] - 50, 150, 40))
    reshuffle_button_rect = pygame.Rect((screen_size[0] // 2 + 10, screen_size[1] - 50, 150, 40))
    
    pygame.draw.rect(window, colors['button_color'], screenshot_button_rect)
    pygame.draw.rect(window, colors['button_color'], reshuffle_button_rect)
    
    screenshot_text = font.render('截圖', True, colors['button_text_color'])
    reshuffle_text = font.render('重排座位', True, colors['button_text_color'])
    
    window.blit(screenshot_text, screenshot_text.get_rect(center=screenshot_button_rect.center))
    window.blit(reshuffle_text, reshuffle_text.get_rect(center=reshuffle_button_rect.center))
    
    return screenshot_button_rect, reshuffle_button_rect

def save_screenshot():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
    if file_path:
        pygame.image.save(window, file_path)

def reshuffle_seats():
    random.shuffle(seats)

def main():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if screenshot_button_rect.collidepoint(event.pos):
                    save_screenshot()
                elif reshuffle_button_rect.collidepoint(event.pos):
                    reshuffle_seats()
        window.fill((0, 0, 0))
        draw_seats()
        draw_podium()
        screenshot_button_rect, reshuffle_button_rect = draw_buttons()
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
