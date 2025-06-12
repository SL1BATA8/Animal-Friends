import streamlit as st

st.title("Kenali hewan is :blue[Animal Friends] :cat:")

import pygame
import sys
import os
import pytesseract
from PIL import Image, ImageFilter, ImageOps, ImageEnhance
import random
import time
import numpy as np
import cv2

# Set path to Tesseract executable (update if necessary)
pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

pygame.init()
pygame.mixer.init()

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BUTTON_COLOR, BUTTON_HOVER = (0, 102, 204), (51, 153, 255)
TEXT_COLOR = (255, 255, 255)
TEXT_HIGHLIGHT = (255, 255, 100)
ERROR_COLOR = (220, 50, 50)

# Screen setup
screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
WIDTH, HEIGHT = screen.get_size()
pygame.display.set_caption("Game Edukasi Hewan")

# Fonts
font = pygame.font.SysFont("Comic Sans MS", 30, bold=True)
big_font = pygame.font.SysFont("Comic Sans MS", 70, bold=True)
input_font = pygame.font.SysFont("Arial", 28)

clock = pygame.time.Clock()

def load_image(path):
    try:
        if os.path.exists(path):
            img = pygame.image.load(path).convert_alpha()
            print(f"Loaded image {path}")
            return img
        else:
            print(f"Image not found: {path}")
            return None
    except Exception as e:
        print(f"Error loading image {path}: {e}")
        return None

def load_sound(path):
    try:
        if os.path.exists(path):
            sound = pygame.mixer.Sound(path)
            print(f"Loaded sound {path}")
            return sound
        else:
            print(f"Sound not found: {path}")
            return None
    except Exception as e:
        print(f"Error loading sound {path}: {e}")
        return None

def load_music(path):
    try:
        if os.path.exists(path):
            pygame.mixer.music.load(path)
            print(f"Loaded music {path}")
            return True
        else:
            print(f"Music not found: {path}")
            return False
    except Exception as e:
        print(f"Error loading music {path}: {e}")
        return False

ASSET_PATHS = {
    "bg_welcome": "c:/Users/Administrator/OneDrive/Dokumen/open.jpg",
    "bg_input": "c:/Users/Administrator/OneDrive/Dokumen/bg2.jpg",
    "bg_darat": "c:/Users/Administrator/Downloads/darat.jpg",
    "bg_air": "c:/Users/Administrator/Downloads/air.png",
    "bg_darat_dan_air": "c:/Users/Administrator/Downloads/ad.jpg",
    "bg_tanah": "c:/Users/Administrator/Downloads/tanah.jpeg",
    "bg_tebak": "c:/Users/Administrator/Downloads/blue.jpg",
    "welcome_music": "c:/Users/Administrator/Downloads/music.mp3",
    "click_sound": "c:/Users/Administrator/Downloads/klik b.mp3",
    "animal_images": {
        "kucing": "c:/Users/Administrator/Downloads/kucing.png",
        "anjing": "c:/Users/Administrator/Downloads/dog.png",
        "singa": "c:/Users/Administrator/Downloads/leon.png",
        "gajah": "c:/Users/Administrator/Downloads/gajah.png",
        "ikan": "c:/Users/Administrator/Downloads/ikan.png",
        "jangkrik": "c:/Users/Administrator/Downloads/jangkrik.png",
        "cacing": "c:/Users/Administrator/Downloads/cacing.png",
        "capung": "c:/Users/Administrator/Downloads/capung.png",
        "tikus": "c:/Users/Administrator/Downloads/rat.png",
        "ulat": "c:/Users/Administrator/Downloads/ulat.png",
        "siput": "c:/Users/Administrator/Downloads/siput.png",
        "ular": "c:/Users/Administrator/Downloads/ular.png",
        "belalang": "c:/Users/Administrator/Downloads/belalang.png",
        "kura-kura": "c:/Users/Administrator/Downloads/kura.png",
        "sapi": "c:/Users/Administrator/Downloads/sapi.png",
        "hamster": "c:/Users/Administrator/Downloads/hamster.png",
        "kelinci": "c:/Users/Administrator/Downloads/rabit.png",
        "panda": "c:/Users/Administrator/Downloads/panda.png",
        "zebra": "c:/Users/Administrator/Downloads/zebra.png",
        "jerapah": "c:/Users/Administrator/Downloads/jerapah.png",
        "rusa": "c:/Users/Administrator/Downloads/rusa.png",
        "lebah": "c:/Users/Administrator/Downloads/bee.png",
        "katak": "c:/Users/Administrator/Downloads/frog.png",
        "unta": "c:/Users/Administrator/Downloads/unta.png",
        "gagak": "c:/Users/Administrator/Downloads/gagak.png",
        "bebek": "c:/Users/Administrator/Downloads/bebek.png",
        "badak": "c:/Users/Administrator/Downloads/badak.png",
        "gorila": "c:/Users/Administrator/Downloads/gorila.png",
        "monyet": "c:/Users/Administrator/Downloads/kera.png",
        "domba": "c:/Users/Administrator/Downloads/domba.png",
        "kupu-kupu": "c:/Users/Administrator/Downloads/kupu.png",
        "burung": "c:/Users/Administrator/Downloads/bird.png",
        "koala": "c:/Users/Administrator/Downloads/koala.png",
        "buaya": "c:/Users/Administrator/Downloads/buaya.png",
        "serigala": "c:/Users/Administrator/Downloads/wolf.png",
        "rubah": "c:/Users/Administrator/Downloads/rubah.png",
        "musang": "c:/Users/Administrator/Downloads/musang.png",
        "ayam": "c:/Users/Administrator/Downloads/ayam.png",
        "hiu": "c:/Users/Administrator/Downloads/hiu.png",
        "semut": "c:/Users/Administrator/Downloads/ant.png",
        "kuda": "c:/Users/Administrator/Downloads/kuda.png",
        "paus": "c:/Users/Administrator/Downloads/paus.png",
        "harimau": "c:/Users/Administrator/Downloads/tiger.png",
        "babi": "c:/Users/Administrator/Downloads/pig.png",
        "kambing": "c:/Users/Administrator/Downloads/goat.png",
        "merak": "c:/Users/Administrator/Downloads/merak.png",
        "beruang": "c:/Users/Administrator/Downloads/bear.png",
        "kepiting": "c:/Users/Administrator/Downloads/crab.png",
        "udang": "c:/Users/Administrator/Downloads/udang.png",
        "cumi-cumi": "c:/Users/Administrator/Downloads/cumi.png",
        "penyu": "c:/Users/Administrator/Downloads/penyu.png",
        "lumba-lumba": "c:/Users/Administrator/Downloads/lumba.png",
        "gurita": "c:/Users/Administrator/Downloads/gurita.png",
        "ubur-ubur": "c:/Users/Administrator/Downloads/ubur.png",
        "kerbau": "c:/Users/Administrator/Downloads/kerbau.png",
        "kecoa": "c:/Users/Administrator/Downloads/kecoa.png",
        "lalat": "c:/Users/Administrator/Downloads/lalat.png",
        "laba-laba": "c:/Users/Administrator/Downloads/laba.png",
        "nyamuk": "c:/Users/Administrator/Downloads/nyamuk.png",
    },
}

class Game:
    def __init__(self):
        self.bg_welcome = load_image(ASSET_PATHS["bg_welcome"])
        self.bg_input = load_image(ASSET_PATHS["bg_input"])
        self.bg_darat = load_image(ASSET_PATHS["bg_darat"])
        self.bg_air = load_image(ASSET_PATHS["bg_air"])
        self.bg_darat_dan_air = load_image(ASSET_PATHS["bg_darat_dan_air"])
        self.bg_tanah = load_image(ASSET_PATHS["bg_tanah"])
        self.bg_tebak = load_image(ASSET_PATHS["bg_tebak"])
        self.welcome_music_path = ASSET_PATHS["welcome_music"]
        self.click_sound = load_sound(ASSET_PATHS["click_sound"])
        if self.bg_welcome: self.bg_welcome = pygame.transform.smoothscale(self.bg_welcome, (WIDTH, HEIGHT))
        if self.bg_input: self.bg_input = pygame.transform.smoothscale(self.bg_input, (WIDTH, HEIGHT))
        if self.bg_darat: self.bg_darat = pygame.transform.smoothscale(self.bg_darat, (WIDTH, HEIGHT))
        if self.bg_air: self.bg_air = pygame.transform.smoothscale(self.bg_air, (WIDTH, HEIGHT))
        if self.bg_tanah: self.bg_tanah = pygame.transform.smoothscale(self.bg_tanah, (WIDTH, HEIGHT))
        if self.bg_darat_dan_air: self.bg_darat_dan_air = pygame.transform.smoothscale(self.bg_darat_dan_air, (WIDTH, HEIGHT))
        if self.bg_tebak: self.bg_tebak = pygame.transform.smoothscale(self.bg_tebak, (WIDTH, HEIGHT))
        
        self.animal_images = {}
        for name, path in ASSET_PATHS["animal_images"].items():
            img = load_image(path)
            if img:
                self.animal_images[name] = img
            # else:
            #     print(f"Warning: Missing image for '{name}', excluding from game.")

        self.animal_habitats = {
            "kucing": "darat", "anjing": "darat", "singa": "darat",
            "gajah": "darat", "beruang": "darat", "jangkrik": "darat",
            "capung": "darat", "tikus": "darat", "ulat": "darat",
            "ular": "darat", "belalang": "darat", "sapi": "darat",
            "hamster": "darat", "kelinci": "darat", "panda": "darat",
            "zebra": "darat", "jerapah": "darat", "rusa": "darat",
            "lebah": "darat", "unta": "darat", "gagak": "darat",
            "bebek": "darat", "badak": "darat", "gorila": "darat",
            "monyet": "darat", "domba": "darat", "kupu-kupu": "darat",
            "burung": "darat", "koala": "darat", "serigala": "darat",
            "rubah": "darat", "musang": "darat", "ayam": "darat",
            "semut": "darat", "kuda": "darat", "harimau": "darat",
            "babi": "darat", "merak": "darat", "ikan": "air",
            "paus": "air", "hiu": "air", "cumi-cumi": "air",
            "udang": "air", "lumba-lumba": "air", "gurita": "air",
            "kambing": "darat", "ubur-ubur": "air", "kepiting": "air",
            "penyu": "air", "kerbau": "darat", "cacing": "tanah",
            "katak": "darat dan air", "buaya": "darat dan air",
            "siput": "darat dan air", "kura-kura": "darat dan air",
            "kecoa": "darat", "lalat": "darat", 
            "laba-laba": "darat", "nyamuk": "darat"
        }

        self.animal_types = {
            "kucing": "Melahirkan (vivipar)", "anjing": "Melahirkan (vivipar)",
            "singa": "Melahirkan (vivipar)", "gajah": "Melahirkan (vivipar)",
            "beruang": "Melahirkan (vivipar)", "sapi": "Melahirkan (vivipar)",
            "tikus": "Melahirkan (vivipar)", "hamster": "Melahirkan (vivipar)",
            "kelinci": "Melahirkan (vivipar)", "panda": "Melahirkan (vivipar)",
            "zebra": "Melahirkan (vivipar)", "jerapah": "Melahirkan (vivipar)",
            "rusa": "Melahirkan (vivipar)", "unta": "Melahirkan (vivipar)",
            "badak": "Melahirkan (vivipar)", "gorila": "Melahirkan (vivipar)",
            "monyet": "Melahirkan (vivipar)", "domba": "Melahirkan (vivipar)",
            "koala": "Melahirkan (vivipar)", "serigala": "Melahirkan (vivipar)",
            "rubah": "Melahirkan (vivipar)", "musang": "Melahirkan (vivipar)",
            "kuda": "Melahirkan (vivipar)", "harimau": "Melahirkan (vivipar)",
            "babi": "Melahirkan (vivipar)", "lumba-lumba": "Melahirkan (vivipar)",
            "ikan": "Bertelur (ovipar)", "merak": "Bertelur (ovipar)",
            "semut": "Bertelur (ovipar)", "ayam": "Bertelur (ovipar)",
            "buaya": "Bertelur (ovipar)", "burung": "Bertelur (ovipar)",
            "kupu-kupu": "Bertelur (ovipar)", "bebek": "Bertelur (ovipar)",
            "gagak": "Bertelur (ovipar)", "katak": "Bertelur (ovipar)",
            "lebah": "Bertelur (ovipar)", "kura-kura": "Bertelur (ovipar)",
            "belalang": "Bertelur (ovipar)", "capung": "Bertelur (ovipar)",
            "jangkrik": "Bertelur (ovipar)", "siput": "Bertelur (ovipar)",
            "udang": "Bertelur (ovipar)", "kepiting": "Bertelur (ovipar)",
            "cumi-cumi": "Bertelur (ovipar)", "penyu": "Bertelur (ovipar)",
            "gurita": "Bertelur (ovipar)", "ular": "Bertelur dan Melahirkan (ovovivipar)",
            "hiu": "Bertelur dan Melahirkan (ovovivipar)",
            "ubur-ubur": "aseksual dengan cara tunas", "kerbau": "Melahirkan (vivipar)",
            "cacing": "seksual dan aseksual", "paus": "Melahirkan (vivipar)",
            "kambing": "Melahirkan (vivipar)", "kecoa": "Bertelur (metamorfosis tidak sempurna)",
            "lalat": "Bertelur (reproduksi seksual)", "laba-laba": "Bertelur (ovipar)",
            "nyamuk": "Bertelur (ovipar)"
        }

        self.drawing_surface = pygame.Surface((WIDTH, HEIGHT))
        self.drawing_surface.fill(WHITE)
        self.drawing = False
        self.last_pos = None
        self.strokes = []
        self.recognized_text = ""

        self.player_name = None
        self.player_age = None
        self.player_gender = None

        self.running = True

    def play_click(self):
        if self.click_sound:
            self.click_sound.play()

    def scale_image(self, image, max_width, max_height):
        img_w, img_h = image.get_size()
        ratio_w = max_width / img_w
        ratio_h = max_height / img_h
        scale_ratio = min(ratio_w, ratio_h)
        new_w = int(img_w * scale_ratio)
        new_h = int(img_h * scale_ratio)
        return pygame.transform.smoothscale(image, (new_w, new_h))

    def recognize_drawing(self, surface):
        path = "temp_drawing.png"
        try:
            padding = 40
            raw_str = pygame.image.tostring(surface, "RGBA")
            width, height = surface.get_size()
            pil_img = Image.frombytes("RGBA", (width, height), raw_str)

            new_width, new_height = width + 2*padding, height + 2*padding
            padded_img = Image.new("RGBA", (new_width, new_height), (255, 255, 255, 255))
            padded_img.paste(pil_img, (padding, padding))

            gray_img = padded_img.convert("L")

            enhancer_contrast = ImageEnhance.Contrast(gray_img)
            enhanced_img = enhancer_contrast.enhance(2.0)
            enhancer_brightness = ImageEnhance.Brightness(enhanced_img)
            enhanced_img = enhancer_brightness.enhance(1.2)

            np_img = np.array(enhanced_img)
            np_img_cv = cv2.adaptiveThreshold(np_img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                              cv2.THRESH_BINARY_INV, 15, 10)

            kernel = np.ones((3,3), np.uint8)
            morphed = cv2.morphologyEx(np_img_cv, cv2.MORPH_CLOSE, kernel, iterations=1)
            morphed = cv2.morphologyEx(morphed, cv2.MORPH_OPEN, kernel, iterations=1)

            processed_img = Image.fromarray(morphed)

            base_width = 1200
            wpercent = (base_width / float(processed_img.size[0]))
            hsize = int((float(processed_img.size[1]) * float(wpercent)))
            resized_img = processed_img.resize((base_width, hsize), Image.LANCZOS)

            inverted_img = ImageOps.invert(resized_img.convert("L"))

            sharpened_img = inverted_img.filter(ImageFilter.SHARPEN)

            custom_config = r'--oem 3 --psm 6'

            text = pytesseract.image_to_string(sharpened_img, config=custom_config)
            print(f"OCR raw result: {text}")

            # Normalize text: strip, lowercase, remove spaces and unwanted signs
            text = text.strip().lower()
            text = ''.join(c for c in text if c.isalpha())  # keep only letters a-z
            # Additional replacements to fix common OCR errors
            text = text.replace('v', 'u')
            text = text.replace('0', 'o')
            text = text.replace('1', 'i')
            text = text.replace('5', 's')

            def remove_consecutive_duplicates(s):
                if not s:
                    return s
                result = [s[0]]
                for c in s[1:]:
                    if c != result[-1]:
                        result.append(c)
                return ''.join(result)

            normalized_text = remove_consecutive_duplicates(text)
            print(f"OCR normalized result: {normalized_text}")

            matched_key = self.match_animal_key(normalized_text)
            print(f"Matched animal key: {matched_key}")

            return matched_key or normalized_text

        except Exception as e:
            print(f"Error in OCR: {e}")
            return ""
        finally:
            if os.path.exists(path):
                try:
                    os.remove(path)
                except Exception as e:
                    print(f"Could not remove temp image: {e}")

    def match_animal_key(self, recognized_text):
        if not recognized_text:
            return None

        keys = list(self.animal_images.keys())

        def is_repeated_name(key):
            parts = key.split('-')
            return len(parts) == 2 and parts[0] == parts[1]

        for key in keys:
            if is_repeated_name(key):
                part = key.split('-')[0]
                if recognized_text == part:
                    return key

        if recognized_text in keys:
            return recognized_text

        best_match = None
        best_length = 0

        def normalize(s):
            return self._remove_consecutive_duplicates(s.replace('-', ''))

        norm_rec = normalize(recognized_text)

        for key in keys:
            norm_key = normalize(key)
            if norm_key.startswith(norm_rec) or norm_rec.startswith(norm_key):
                if len(norm_key) > best_length:
                    best_length = len(norm_key)
                    best_match = key

        return best_match

    def _remove_consecutive_duplicates(self, s):
        if not s:
            return s
        result = [s[0]]
        for c in s[1:]:
            if c != result[-1]:
                result.append(c)
        return ''.join(result)

    def draw_smooth_line(self, surface, color, start_pos, end_pos, width=8):
        pygame.draw.line(surface, color, start_pos, end_pos, width)

    def button(self, text, rect, hover_color=BUTTON_HOVER, base_color=BUTTON_COLOR):
        mx, my = pygame.mouse.get_pos()
        hovering = rect.collidepoint(mx, my)
        color = hover_color if hovering else base_color
        pygame.draw.rect(screen, color, rect, border_radius=12)
        label = font.render(text, True, TEXT_HIGHLIGHT if hovering else TEXT_COLOR)
        screen.blit(label, (rect.centerx - label.get_width()//2, rect.centery - label.get_height()//2))
        click = pygame.mouse.get_pressed()
        clicked = hovering and click[0]
        return clicked

    def welcome_screen(self):
        if load_music(self.welcome_music_path):
            pygame.mixer.music.play(-1)
        start_time = time.time()
        while time.time() - start_time < 5.0:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            if self.bg_welcome:
                screen.blit(self.bg_welcome, (0,0))
            else:
                screen.fill(WHITE)
            pygame.display.flip()
            clock.tick(30)

    def player_info_input(self):
        input_active = {"name": False, "age": False}
        input_text = {"name": "", "age": ""}
        gender_options = ["Laki-laki", "Perempuan"]
        gender_selected = None

        input_rects = {
            "name": pygame.Rect(WIDTH//2 - 200, 150, 400, 50),
            "age": pygame.Rect(WIDTH//2 - 200, 270, 400, 50),
        }

        button_width = 180
        button_height = 50
        gap = 40
        total_width = 2 * button_width + gap
        gender_start_x = (WIDTH - total_width) // 2
        gender_y = 390

        gender_buttons = []
        for i in range(len(gender_options)):
            rect = pygame.Rect(gender_start_x + i*(button_width+gap), gender_y, button_width, button_height)
            gender_buttons.append(rect)

        continue_button = pygame.Rect(WIDTH//2 - 100, 480, 200, 60)

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    self.play_click()
                    for key in ["name", "age"]:
                        if input_rects[key].collidepoint(event.pos):
                            input_active = {k: False for k in input_active}
                            input_active[key] = True
                            break
                    else:
                        input_active = {k: False for k in input_active}
                    for i, rect in enumerate(gender_buttons):
                        if rect.collidepoint(event.pos):
                            gender_selected = i

                    if continue_button.collidepoint(event.pos):
                        valid_name = len(input_text["name"].strip()) > 0
                        valid_age = input_text["age"].isdigit() and int(input_text["age"]) > 0
                        valid_gender = gender_selected is not None
                        if valid_name and valid_age and valid_gender:
                            self.player_name = input_text["name"].strip()
                            self.player_age = int(input_text["age"])
                            self.player_gender = gender_options[gender_selected]
                            return

                elif event.type == pygame.KEYDOWN:
                    active_key = None
                    for key, active in input_active.items():
                        if active:
                            active_key = key
                            break
                    if active_key:
                        if event.key == pygame.K_BACKSPACE:
                            input_text[active_key] = input_text[active_key][:-1]
                        elif event.key == pygame.K_TAB:
                            keys = ["name", "age"]
                            idx = keys.index(active_key)
                            idx = (idx + 1) % len(keys)
                            input_active = {k: False for k in input_active}
                            input_active[keys[idx]] = True
                        else:
                            if active_key == "age":
                                if event.unicode.isdigit():
                                    input_text[active_key] += event.unicode
                            else:
                                input_text[active_key] += event.unicode
            if self.bg_input:
                screen.blit(self.bg_input, (0,0))
            else:
                screen.fill(WHITE)

            overlay_rect = pygame.Rect(WIDTH//2 - 400, 100, 800, 500)
            s = pygame.Surface((overlay_rect.width, overlay_rect.height), pygame.SRCALPHA)
            s.fill((255,255,255,220))
            screen.blit(s, overlay_rect.topleft)

            label_name = font.render("Nama:", True, BLACK)
            label_age = font.render("Usia:", True, BLACK)
            label_gender = font.render("Jenis Kelamin:", True, BLACK)
            screen.blit(label_name, (input_rects["name"].x, input_rects["name"].y - 40))
            screen.blit(label_age, (input_rects["age"].x, input_rects["age"].y - 40))
            screen.blit(label_gender, (gender_start_x, gender_y - 40))
            
            for key in ["name", "age"]:
                rect = input_rects[key]
                pygame.draw.rect(screen, WHITE, rect, border_radius=12)
                color = BUTTON_HOVER if input_active[key] else BUTTON_COLOR
                pygame.draw.rect(screen, color, rect, 3, border_radius=12)
                display_text = input_text[key]
                txt_surf = input_font.render(display_text, True, BLACK)
                screen.blit(txt_surf, (rect.x+10, rect.y + (rect.height - txt_surf.get_height())//2))
            
            mouse_pos = pygame.mouse.get_pos()
            for i, rect in enumerate(gender_buttons):
                hover = rect.collidepoint(mouse_pos)
                color = BUTTON_HOVER if hover or gender_selected == i else BUTTON_COLOR
                pygame.draw.rect(screen, color, rect, border_radius=12)
                label = font.render(gender_options[i], True, TEXT_COLOR)
                screen.blit(label, (rect.centerx - label.get_width()//2, rect.centery - label.get_height()//2))
            
            valid_name = len(input_text["name"].strip()) > 0
            valid_age = input_text["age"].isdigit() and int(input_text["age"]) > 0
            valid_gender = gender_selected is not None
            
            continue_color = BUTTON_COLOR if (valid_name and valid_age and valid_gender) else (150,150,150)
            pygame.draw.rect(screen, continue_color, continue_button, border_radius=12)
            cont_label = font.render("Lanjutkan", True, TEXT_COLOR)
            screen.blit(cont_label, (continue_button.centerx - cont_label.get_width()//2, continue_button.centery - cont_label.get_height()//2))
            
            if not valid_age and input_text["age"] != "":
                err_surf = font.render("Usia harus berupa angka positif", True, ERROR_COLOR)
                screen.blit(err_surf, (WIDTH//2 - err_surf.get_width()//2, continue_button.bottom + 10))
            
            pygame.display.flip()
            clock.tick(60)

    def reset_drawing(self):
        self.drawing_surface.fill(WHITE)
        self.strokes.clear()
        self.recognized_text = ""
        if load_music(self.welcome_music_path):
            pygame.mixer.music.play(-1)

    def fullscreen_animal_info(self, key):
        running = True
        if key not in self.animal_images:
            return

        image = self.animal_images[key]
        if image is None:
            return
        habitat = self.animal_habitats.get(key, '')
        reproduction = self.animal_types.get(key, '-')

        if habitat.lower() == 'darat' and self.bg_darat:
            background = self.bg_darat
        elif habitat.lower() == 'air' and self.bg_air:
            background = self.bg_air
        elif habitat.lower() == 'darat dan air' and self.bg_darat_dan_air:
            background = self.bg_darat_dan_air
        elif habitat.lower() == 'tanah' and self.bg_tanah:
            background = self.bg_tanah
        else:
            background = None

        max_img_height = int(HEIGHT * 0.4)
        max_img_width = WIDTH - 80

        scaled_img = self.scale_image(image, max_img_width, max_img_height)

        text_margin_x = 40
        text_margin_y = 40

        line_spacing = font.get_height() + 10

        menu_width, menu_height = 180, 50
        back_rect = pygame.Rect(WIDTH - menu_width - 20, HEIGHT - menu_height - 20, menu_width, menu_height)

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if back_rect.collidepoint(event.pos):
                        self.play_click()
                        running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False

            if background:
                screen.blit(background, (0, 0))
            else:
                screen.fill(WHITE)

            img_x = (WIDTH - scaled_img.get_width()) // 2
            img_y = text_margin_y + 3 * line_spacing + 30
            screen.blit(scaled_img, (img_x, img_y))

            name_surf = font.render(key.capitalize(), True, BLACK)
            habitat_surf = font.render(f"Habitat: {habitat.capitalize()}", True, BLACK)
            repro_surf = font.render(f"Berkembang biak: {reproduction}", True, BLACK)

            text_panel_height = 3 * line_spacing + 20
            text_panel_rect = pygame.Rect(10, text_margin_y - 10, WIDTH // 2, text_panel_height)
            s = pygame.Surface((text_panel_rect.width, text_panel_rect.height), pygame.SRCALPHA)
            s.fill((255, 255, 255, 190))
            screen.blit(s, text_panel_rect.topleft)

            screen.blit(name_surf, (text_margin_x, text_margin_y))
            screen.blit(habitat_surf, (text_margin_x, text_margin_y + line_spacing))
            screen.blit(repro_surf, (text_margin_x, text_margin_y + 2 * line_spacing))

            pygame.draw.rect(screen, BUTTON_COLOR, back_rect, border_radius=12)
            back_label = font.render("Menu", True, TEXT_COLOR)
            screen.blit(back_label, (back_rect.centerx - back_label.get_width()//2, back_rect.centery - back_label.get_height()//2))

            pygame.display.flip()
            clock.tick(60)

    def drawing_mode(self):
        self.reset_drawing()
        running = True

        while running:
            screen.fill(WHITE)
            screen.blit(self.drawing_surface, (0,0))

            kenali_rect = pygame.Rect(50, HEIGHT - 130, 120, 50)
            clear_rect = pygame.Rect(200, HEIGHT - 130, 120, 50)
            undo_rect = pygame.Rect(350, HEIGHT - 130, 120, 50)
            back_rect = pygame.Rect(WIDTH - 220, HEIGHT - 130, 180, 50)

            kenali_clicked = self.button("Kenali", kenali_rect)
            clear_clicked = self.button("Clear", clear_rect)
            undo_clicked = self.button("Undo", undo_rect)
            back_clicked = self.button("Menu", back_rect)

            recog_box = pygame.Rect(50, HEIGHT - 230, WIDTH - 350, 80)
            pygame.draw.rect(screen, (230,230,230), recog_box, border_radius=12)
            pygame.draw.rect(screen, BLACK, recog_box, 2, border_radius=12)

            recog_lines = []
            if self.recognized_text.strip():
                words = self.recognized_text.strip().split()
                line = ""
                for word in words:
                    test_line = line + word + " "
                    if font.size(test_line)[0] > recog_box.width-20:
                        recog_lines.append(line)
                        line = word + " "
                    else:
                        line = test_line
                if line:
                    recog_lines.append(line)
            else:
                recog_lines.append("Teks hasil pengenalan akan muncul di sini...")

            for i, line in enumerate(recog_lines):
                text_surf = font.render(line.strip(), True, BLACK)
                screen.blit(text_surf, (recog_box.x+10, recog_box.y+10 + i*(font.get_height()+2)))

            animal_info_area = pygame.Rect(WIDTH-400, HEIGHT-230, 350, 180)
            key = self.recognized_text.strip()

            if key in self.animal_images:
                habitat = self.animal_habitats.get(key, '').lower()                
                if habitat == 'darat' and self.bg_darat:
                    screen.blit(self.bg_darat, animal_info_area.topleft)
                elif habitat == 'air' and self.bg_air:
                    screen.blit(self.bg_air, animal_info_area.topleft)
                elif habitat == 'darat dan air' and self.bg_darat_dan_air:
                    screen.blit(self.bg_darat_dan_air, animal_info_area.topleft)
                elif habitat == 'tanah' and self.bg_tanah:
                    screen.blit(self.bg_tanah, animal_info_area.topleft)
                else:
                    pygame.draw.rect(screen, (240,240,240), animal_info_area, border_radius=12)

                text_bg_rect = pygame.Rect(animal_info_area.x, animal_info_area.y, animal_info_area.width, 100)
                s = pygame.Surface((text_bg_rect.width, text_bg_rect.height), pygame.SRCALPHA)
                s.fill((255,255,255,200))
                screen.blit(s, text_bg_rect.topleft)
                pygame.draw.rect(screen, BLACK, animal_info_area, 2, border_radius=12)

                name_surf = font.render(key.capitalize(), True, BLACK)
                habitat_surf = font.render(f"Habitat: {habitat.capitalize()}", True, BLACK)
                repro_surf = font.render(f"Jenis Melahirkan: {self.animal_types.get(key,'-')}", True, BLACK)

                screen.blit(name_surf, (animal_info_area.x+10, animal_info_area.y+10))
                screen.blit(habitat_surf, (animal_info_area.x+10, animal_info_area.y+50))
                screen.blit(repro_surf, (animal_info_area.x+10, animal_info_area.y+90))

                animal_img = self.animal_images[key]
                if animal_img:
                    scaled_img = self.scale_image(animal_img, 320, 70)
                    img_x = animal_info_area.x + (animal_info_area.width - scaled_img.get_width()) // 2
                    img_y = animal_info_area.y + 100 + (animal_info_area.height - 100 - scaled_img.get_height()) // 2
                    screen.blit(scaled_img, (img_x, img_y))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE or back_clicked:
                        self.play_click()
                        running = False
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if kenali_rect.collidepoint(event.pos):
                        self.play_click()
                        ocr_result = self.recognize_drawing(self.drawing_surface)
                        if ocr_result.strip():
                            if self.recognized_text:
                                self.recognized_text += " "
                            self.recognized_text += ocr_result.strip()
                            if ocr_result.strip() in self.animal_images:
                                self.fullscreen_animal_info(ocr_result.strip())
                                self.reset_drawing()
                        else:
                            self.recognized_text += " (tidak ada teks terdeteksi)"
                    elif clear_rect.collidepoint(event.pos):
                        self.play_click()
                        self.reset_drawing()
                    elif undo_rect.collidepoint(event.pos):
                        self.play_click()
                        if self.strokes:
                            self.strokes.pop()
                            self.drawing_surface.fill(WHITE)
                            for stroke in self.strokes:
                                if len(stroke) > 1:
                                    for i in range(len(stroke)-1):
                                        self.draw_smooth_line(self.drawing_surface, BLACK, stroke[i], stroke[i+1], width=8)
                    elif back_rect.collidepoint(event.pos):
                        self.play_click()
                        running = False
                    else:
                        self.drawing = True
                        self.last_pos = event.pos
                        self.strokes.append([event.pos])
                elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    self.drawing = False
                elif event.type == pygame.MOUSEMOTION and self.drawing:
                    if self.last_pos is not None:
                        self.draw_smooth_line(self.drawing_surface, BLACK, self.last_pos, event.pos, width=8)
                        if self.strokes:
                            self.strokes[-1].append(event.pos)
                    self.last_pos = event.pos

            pygame.display.flip()
            clock.tick(60)

    def tebak_hewan_mode(self):
        clock = pygame.time.Clock()
        animal_keys = [key for key, img in self.animal_images.items() if img is not None]
        if len(animal_keys) < 4:
            print("Minimal 4 hewan dengan gambar diperlukan untuk mode tebak.")
            return
        play = True
        while play:
            correct_animal = random.choice(animal_keys)
            wrong_choices = random.sample([a for a in animal_keys if a != correct_animal], 3)
            options = wrong_choices + [correct_animal]
            random.shuffle(options)
            answered = False
            result_text = ""
            result_display_time = 0
            back_rect = pygame.Rect(WIDTH - 220, HEIGHT - 70, 180, 50)
            while True:
                if self.bg_tebak:
                    screen.blit(self.bg_tebak, (0, 0))
                else:
                    screen.fill(WHITE)

                prompt = font.render("Tebak Hewan Apa Ini?", True, BLACK)
                screen.blit(prompt, (WIDTH // 2 - prompt.get_width() // 2, 50))

                correct_img = self.animal_images.get(correct_animal)
                if correct_img is not None:
                    scaled_img = self.scale_image(correct_img, 300, 300)
                    screen.blit(scaled_img, (WIDTH // 2 - scaled_img.get_width() // 2, 200))

                mouse = pygame.mouse.get_pos()
                button_rects = []
                for i, option in enumerate(options):
                    x = WIDTH // 2 - 220 + (i % 2) * 240
                    y = 520 + (i // 2) * 80
                    rect = pygame.Rect(x, y, 200, 60)
                    hover = rect.collidepoint(mouse)
                    color = BUTTON_HOVER if hover else BUTTON_COLOR
                    pygame.draw.rect(screen, color, rect, border_radius=10)
                    label = font.render(option.capitalize(), True, (255, 255, 100) if hover else TEXT_COLOR)
                    screen.blit(label, (rect.centerx - label.get_width() // 2, rect.centery - label.get_height() // 2))
                    button_rects.append((rect, option))

                back_button_color = BUTTON_HOVER if back_rect.collidepoint(mouse) else BUTTON_COLOR
                pygame.draw.rect(screen, back_button_color, back_rect, border_radius=10)
                back_label = font.render("Menu", True, TEXT_COLOR)
                screen.blit(back_label, (back_rect.centerx - back_label.get_width() // 2, back_rect.centery - back_label.get_height() // 2))

                if answered:
                    color_result = (0, 150, 0) if result_text.startswith("Betul") else (200, 0, 0)
                    result_surf = big_font.render(result_text, True, color_result)
                    screen.blit(result_surf, (WIDTH // 2 - result_surf.get_width() // 2, HEIGHT - result_surf.get_height() - 40))
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()

                    elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                        pos = event.pos
                        if back_rect.collidepoint(pos):
                            self.play_click()
                            play = False
                            return
                        if not answered:
                            self.play_click()
                            for rect, opt in button_rects:
                                if rect.collidepoint(pos):
                                    if opt == correct_animal:
                                        result_text = "Betul! Kamu pintar!"
                                    else:
                                        result_text = f"Salah! Jawaban benar: {correct_animal.capitalize()}"
                                    answered = True
                                    result_display_time = pygame.time.get_ticks()
                                    break

                if answered:
                    if pygame.time.get_ticks() - result_display_time > 3000:
                        break

                pygame.display.flip()
                clock.tick(60)

    def main_menu(self):
        clock = pygame.time.Clock()
        selected_mode = None

        show_instructions = True

        while show_instructions:
            screen.fill(WHITE)
            title = big_font.render("Instruksi Permainan", True, BLACK)
            screen.blit(title, (WIDTH//2 - title.get_width()//2, 60))

            instructions = [
                "1. Pilih 'Tulis Hewan' untuk menulis nama hewan dan akan mengenali tulisan.",
                "2. Pilih 'Tebak Hewan' untuk menebak nama hewan dari gambar.",
                "3. Menulis bisa mengunakan stylus pen.",
                "4. Gunakan tombol Menu di setiap layar untuk kembali.",
                "Klik untuk melanjutkan ke menu utama.",
            ]

            for i, line in enumerate(instructions):
                instr_surf = font.render(line, True, BLACK)
                screen.blit(instr_surf, (50, 180 + i * 50))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    self.play_click()
                    show_instructions = False

            pygame.display.flip()
            clock.tick(30)

        while selected_mode is None:
            screen.fill(WHITE)
            title = font.render("Pilih Mode Permainan", True, BLACK)
            screen.blit(title, (WIDTH//2 - title.get_width()//2, 100))
            mx, my = pygame.mouse.get_pos()

            rect_gambar = pygame.Rect(WIDTH//2 - 170, HEIGHT//2 - 40, 340, 70)
            rect_tebak = pygame.Rect(WIDTH//2 - 170, HEIGHT//2 + 60, 340, 70)

            color_gambar = BUTTON_HOVER if rect_gambar.collidepoint(mx, my) else BUTTON_COLOR
            pygame.draw.rect(screen, color_gambar, rect_gambar, border_radius=12)
            label_gambar = font.render("Tulis Hewan", True, TEXT_COLOR)
            screen.blit(label_gambar, (rect_gambar.centerx - label_gambar.get_width()//2, rect_gambar.centery - label_gambar.get_height()//2))

            color_tebak = BUTTON_HOVER if rect_tebak.collidepoint(mx, my) else BUTTON_COLOR
            pygame.draw.rect(screen, color_tebak, rect_tebak, border_radius=12)
            label_tebak = font.render("Tebak Hewan", True, TEXT_COLOR)
            screen.blit(label_tebak, (rect_tebak.centerx - label_tebak.get_width()//2, rect_tebak.centery - label_tebak.get_height()//2))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if rect_gambar.collidepoint(event.pos):
                        self.play_click()
                        selected_mode = "tulis"
                    elif rect_tebak.collidepoint(event.pos):
                        self.play_click()
                        selected_mode = "tebak"

            pygame.display.flip()
            clock.tick(30)
        return selected_mode

    def run(self):
        self.welcome_screen()
        self.player_info_input()
        if load_music(self.welcome_music_path):
            pygame.mixer.music.play(-1)
        while self.running:
            mode = self.main_menu()
            if mode == "tulis":
                self.drawing_mode()
            elif mode == "tebak":
                self.tebak_hewan_mode()

if __name__ == "__main__":
    game = Game()
    game.run()
