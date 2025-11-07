import os
import random
from PIL import Image
import gradio as gr

# === 1. Путь к текущей папке (где лежат изображения) ===
IMAGE_DIR = "."

# === 2. Собираем все файлы изображений ===
image_files = [f for f in os.listdir(IMAGE_DIR) if f.lower().endswith(('.jpg', '.jpeg', '.png'))]

def get_animal_name(filename):
    """Извлекает название животного из имени файла"""
    name = filename.split('.')[0].lower()
    if 'cat' in name:
        return "Кошка 🐱"
    elif 'dog' in name:
        return "Собака 🐶"
    elif 'elephant' in name:
        return "Слон 🐘"
    elif 'horse' in name:
        return "Лошадь 🐴"
    elif 'lion' in name:
        return "Лев 🦁"
    else:
        return "Неизвестное животное ❓"

def show_random_animal():
    """Выбирает случайное изображение и показывает"""
    if not image_files:
        return None, "Нет изображений в папке!"
    
    file = random.choice(image_files)
    img = Image.open(os.path.join(IMAGE_DIR, file)).resize((350, 350))
    label = get_animal_name(file)
    return img, label

# === 3. Создаём интерфейс Gradio ===
with gr.Blocks(theme=gr.themes.Soft()) as demo:
    gr.Markdown("<h1 style='text-align:center;'>🐾 Просмотр животных</h1>")
    gr.Markdown("Нажмите кнопку, чтобы увидеть случайное животное.")
    
    image_output = gr.Image(type="pil", label="Изображение животного")
    label_output = gr.Textbox(label="Название", interactive=False)
    
    btn = gr.Button("Показать другое животное", variant="primary")
    btn.click(fn=show_random_animal, outputs=[image_output, label_output])

# === 4. Запуск ===
if __name__ == "__main__":
    demo.launch()
