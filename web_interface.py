#!/usr/bin/env python3
"""
ASCII Photo Mask - Web Interface
Beautiful web UI for generating ASCII photo masks using Gradio.
"""

import gradio as gr
import tempfile
from pathlib import Path
from ascii_art import ASCIIPhotoMask, Config


def generate_ascii_art(
    image,
    char_width: int,
    font_size: int,
    brightness: float,
    contrast: float,
    randomize: bool,
    bold: bool
):
    """
    Generate ASCII photo mask from uploaded image.

    Args:
        image: Uploaded image from Gradio
        char_width: Number of characters across width
        font_size: Size of each character in pixels
        brightness: Brightness multiplier
        contrast: Contrast multiplier
        randomize: Enable randomization for organic look
        bold: Enable bold characters

    Returns:
        Path to generated ASCII art image
    """
    if image is None:
        return None

    try:
        # Create configuration
        config = Config(
            char_width=char_width,
            font_size=font_size,
            brightness_multiplier=brightness,
            contrast_multiplier=contrast,
            enable_randomization=randomize,
            bold_enabled=bold,
        )

        # Create generator
        generator = ASCIIPhotoMask(config)

        # Create temporary output file
        output_file = tempfile.NamedTemporaryFile(
            delete=False,
            suffix='.png',
            prefix='ascii_art_'
        )
        output_path = Path(output_file.name)
        output_file.close()

        # Generate ASCII art
        input_path = Path(image)
        generator.generate(input_path, output_path)

        return str(output_path)

    except Exception as e:
        print(f"Error generating ASCII art: {e}")
        return None


# Create Gradio interface
with gr.Blocks(title="ASCII Photo Mask", theme=gr.themes.Soft()) as demo:
    gr.Markdown(
        """
        # 🎨 ASCII Photo Mask Generator

        Transform your photos into stunning ASCII art where images shine through character-shaped masks.

        Upload an image and adjust the settings below to create your custom ASCII art!
        """
    )

    with gr.Row():
        with gr.Column(scale=1):
            # Input section
            gr.Markdown("### 📤 Input")
            image_input = gr.Image(
                type="filepath",
                label="Upload Your Photo",
                sources=["upload", "clipboard"]
            )

            gr.Markdown("### ⚙️ Settings")

            with gr.Accordion("Character Settings", open=True):
                char_width = gr.Slider(
                    minimum=20,
                    maximum=200,
                    value=80,
                    step=10,
                    label="Character Width",
                    info="Number of characters across the width (more = smaller characters)"
                )

                font_size = gr.Slider(
                    minimum=8,
                    maximum=60,
                    value=25,
                    step=1,
                    label="Font Size",
                    info="Size of each character in pixels"
                )

            with gr.Accordion("Visual Enhancement", open=True):
                brightness = gr.Slider(
                    minimum=1.0,
                    maximum=3.0,
                    value=1.8,
                    step=0.1,
                    label="Brightness",
                    info="Brightness multiplier (higher = lighter image)"
                )

                contrast = gr.Slider(
                    minimum=1.0,
                    maximum=2.0,
                    value=1.3,
                    step=0.1,
                    label="Contrast",
                    info="Contrast multiplier (higher = more pop)"
                )

            with gr.Accordion("Style Options", open=True):
                randomize = gr.Checkbox(
                    value=True,
                    label="Organic Randomization",
                    info="Vary character sizes and positions for hand-crafted look"
                )

                bold = gr.Checkbox(
                    value=True,
                    label="Bold Characters",
                    info="Make characters thicker and more prominent"
                )

            # Presets
            gr.Markdown("### 🎯 Quick Presets")
            with gr.Row():
                preset_detailed = gr.Button("📖 Detailed (120x18)", size="sm")
                preset_medium = gr.Button("⚖️ Medium (80x25)", size="sm")
                preset_poster = gr.Button("🖼️ Poster (40x55)", size="sm")

            # Generate button
            generate_btn = gr.Button("✨ Generate ASCII Art", variant="primary", size="lg")

        with gr.Column(scale=1):
            # Output section
            gr.Markdown("### 🎨 Result")
            image_output = gr.Image(
                label="ASCII Photo Mask",
                type="filepath"
            )

            gr.Markdown(
                """
                ### 💡 Tips

                - **For portraits**: Use medium to large characters (40-80 width)
                - **For landscapes**: Smaller characters work better (100-120 width)
                - **Dark photos**: Increase brightness (2.0+)
                - **Poster prints**: Use large characters (40-60 width, 50-60 size)
                """
            )

    # Preset button handlers
    preset_detailed.click(
        fn=lambda: (120, 18),
        outputs=[char_width, font_size]
    )

    preset_medium.click(
        fn=lambda: (80, 25),
        outputs=[char_width, font_size]
    )

    preset_poster.click(
        fn=lambda: (40, 55),
        outputs=[char_width, font_size]
    )

    # Generate button handler
    generate_btn.click(
        fn=generate_ascii_art,
        inputs=[
            image_input,
            char_width,
            font_size,
            brightness,
            contrast,
            randomize,
            bold
        ],
        outputs=image_output
    )

    gr.Markdown(
        """
        ---

        Made with ASCII Photo Mask | [GitHub](https://github.com/0x0ndra/ascii-photo-mask)
        """
    )


if __name__ == "__main__":
    demo.launch(
        share=False,  # Set to True to create public link
        server_name="127.0.0.1",
        server_port=7860
    )
