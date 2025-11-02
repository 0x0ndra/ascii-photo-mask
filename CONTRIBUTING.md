# Contributing to ASCII Photo Mask

First off, thank you for considering contributing to ASCII Photo Mask! It's people like you that make this project better for everyone.

## Code of Conduct

This project and everyone participating in it is governed by respect and professionalism. Please be considerate and respectful in your interactions.

## How Can I Contribute?

### Reporting Bugs

Before creating bug reports, please check the existing issues to avoid duplicates. When you create a bug report, include as many details as possible:

- **Use a clear and descriptive title**
- **Describe the exact steps to reproduce the problem**
- **Provide specific examples** (command-line arguments, input images, etc.)
- **Describe the behavior you observed** and what you expected
- **Include screenshots** if relevant
- **Provide your environment details** (OS, Python version, Pillow version)

### Suggesting Enhancements

Enhancement suggestions are tracked as GitHub issues. When creating an enhancement suggestion:

- **Use a clear and descriptive title**
- **Provide a detailed description** of the suggested enhancement
- **Explain why this enhancement would be useful**
- **List some examples** of where this enhancement could be used

### Pull Requests

1. **Fork the repository** and create your branch from `main`
2. **Follow the coding standards** outlined below
3. **Test your changes** thoroughly
4. **Update documentation** if needed (README, docstrings, etc.)
5. **Write a clear commit message** describing your changes

#### Coding Standards

This project follows these principles:

- **DRY** (Don't Repeat Yourself): Avoid code duplication
- **LEGO**: Build modular, composable components
- **KISS** (Keep It Simple, Stupid): Prefer simple, readable solutions
- **Type Hints**: Include type annotations for function signatures
- **Docstrings**: Document all public classes and methods

##### Code Style

- Follow [PEP 8](https://pep8.org/) Python style guide
- Use 4 spaces for indentation (no tabs)
- Maximum line length: 100 characters
- Use descriptive variable names
- Add comments for complex logic

##### Example

```python
def process_image(
    img: Image.Image,
    brightness: float,
    contrast: float
) -> Image.Image:
    """
    Process image with brightness and contrast adjustments.

    Args:
        img: Source image
        brightness: Brightness multiplier (1.0 = no change)
        contrast: Contrast multiplier (1.0 = no change)

    Returns:
        Processed image
    """
    # Apply brightness enhancement
    enhancer = ImageEnhance.Brightness(img)
    img = enhancer.enhance(brightness)

    # Apply contrast enhancement
    enhancer = ImageEnhance.Contrast(img)
    img = enhancer.enhance(contrast)

    return img
```

### Testing

Before submitting a pull request, test your changes with various configurations:

```bash
# Test web interface
python3 web_interface.py
# Then test in browser at http://localhost:7860

# Test CLI basic functionality
python3 ascii_art.py test_image.jpg

# Test presets (Detailed, Medium, Bold)
python3 ascii_art.py test_image.jpg -w 120 -s 18  # Detailed
python3 ascii_art.py test_image.jpg -w 60 -s 30   # Medium
python3 ascii_art.py test_image.jpg -w 40 -s 55   # Bold

# Test randomization toggle
python3 ascii_art.py test_image.jpg --no-random

# Test bold toggle
python3 ascii_art.py test_image.jpg --no-bold

# Test brightness/contrast
python3 ascii_art.py test_image.jpg -b 2.0 -c 1.5
```

### Documentation

- Update README.md if you add new features
- Add docstrings to new functions/classes
- Update help text in argparse if you add CLI arguments
- Add examples for new features

## Project Structure

```
ascii-photo-mask/
├── ascii_art.py          # Core algorithm (CLI)
├── web_interface.py      # Web UI (Gradio)
├── README.md             # Project documentation
├── CONTRIBUTING.md       # This file
├── LICENSE               # MIT License
├── requirements.txt      # Python dependencies
├── setup.py              # Package setup
├── .gitignore           # Git ignore rules
├── .env.example         # Environment config template
├── DEPLOYMENT.example.md # Deployment guide template
└── examples/            # Example images (before/after)
    ├── before.jpeg
    ├── after.png
    ├── example_original.jpg
    └── example_output.png
```

## Development Setup

1. Clone your fork:
```bash
git clone https://github.com/YOUR_USERNAME/ascii-photo-mask.git
cd ascii-photo-mask
```

2. Create a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a branch for your changes:
```bash
git checkout -b feature/your-feature-name
```

## Commit Messages

Write clear, concise commit messages:

- Use present tense ("Add feature" not "Added feature")
- Use imperative mood ("Move cursor to..." not "Moves cursor to...")
- Limit first line to 72 characters
- Reference issues and pull requests when relevant

Examples:
```
Add custom character set support via --chars argument

Fix character overlap issue with large font sizes

Update README with new examples
```

## Questions?

Feel free to open an issue with the "question" label if you have any questions about contributing!

---

Thank you for contributing!
