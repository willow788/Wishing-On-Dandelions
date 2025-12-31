<div align="center">

# 🌼 Wishing On Dandelions 🌼

### *Because who needs to study when you can code recursive trees?*

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Turtle Graphics](https://img.shields.io/badge/Turtle-Graphics-green?style=for-the-badge)
![Procrastination](https://img.shields.io/badge/Procrastination-Level%20100-ff69b4?style=for-the-badge)

<img src="./Demonstration/Dandelions.png" alt="Dandelion Tree" width="600px"/>

*A recursive fractal tree generator built during New Year's Eve instead of celebrating* 🎆

---

</div>

## ✨ What Is This?

Instead of studying or popping champagne at midnight, I decided to create a mesmerizing recursive tree using Python's `turtle` module.  Because nothing says "Happy New Year" quite like recursion and fractal patterns! 🎉

This project draws a beautiful branching tree structure with orange blossoms, reminiscent of dandelions swaying in the wind – hence the poetic name. 

## 🎨 Features

- 🌳 **Recursive Fractal Algorithm** – Watch the tree grow branch by branch
- 🎨 **Beautiful Color Palette** – Brown branches, orange blossoms, black night sky
- 🐢 **Turtle Graphics** – Because sometimes the classics are the best
- ⚡ **Adjustable Speed & Depth** – Customize your tree to your liking
- 💭 **Meditative Procrastination** – The perfect excuse to avoid your responsibilities

## 🚀 Quick Start

### Prerequisites

```bash
# Just Python!  No external dependencies needed
python --version  # Python 3.x
```

### Installation

```bash
# Clone this repository
git clone https://github.com/willow788/Wishing-On-Dandelions.git

# Navigate to the directory
cd Wishing-On-Dandelions/Code

# Run the magic
python main.py
```

## 🎯 How It Works

The heart of this project is a simple yet elegant recursive function: 

```python
def tree(i):
    if i < 10:
        return
    else: 
        t.forward(i)
        t.color("orange")
        t.circle(2)      # Draw a blossom
        t.color("brown")
        t.left(30)
        tree(3 * i/4)    # Left branch (recursion!)
        t.right(60)
        tree(3 * i/4)    # Right branch (more recursion!)
        t.left(30)
        t.backward(i)
```

Each branch splits into two smaller branches, creating a beautiful fractal pattern that resembles nature's own design!

## 🎨 Customization Ideas

Want to make it your own? Try tweaking these parameters:

- **`t.speed(100)`** – Change drawing speed (1-100)
- **`tree(100)`** – Adjust initial branch length for bigger/smaller trees
- **`t.left(30)` & `t.right(60)`** – Modify angles for different branch patterns
- **`3 * i/4`** – Change the ratio for bushier or sparser trees
- **Colors** – Make it a cherry blossom tree, autumn leaves, or whatever you imagine!

## 📸 Gallery

<div align="center">

### The Result

![Dandelion Tree Visualization](./Demonstration/Dandelions.png)

*A fractal tree born from procrastination and pure Python*

</div>

## 🤔 Why "Wishing On Dandelions"? 

Dandelions symbolize wishes, dreams, and new beginnings.  What better way to welcome the new year than by creating something beautiful instead of cramming for exams? Sometimes the best memories come from spontaneous acts of creativity! 🌟

## 🎓 What I Learned (Instead of Studying)

- ✅ Recursive algorithms and fractal geometry
- ✅ Python's turtle graphics module
- ✅ That procrastination can be productive too
- ✅ How to make branches look organic with simple math
- ❌ Whatever was on the exam

## 📝 License

This project is open source and available under the MIT License.  Feel free to fork, modify, and create your own procrastination masterpieces!

## 🌟 Acknowledgments

- **My textbooks** – for being so boring that I chose to code instead
- **New Year's Eve** – for providing the perfect excuse
- **Recursion** – for making beautiful patterns possible
- **Coffee** – the real MVP ☕

---

<div align="center">

### 💫 Made with ❤️ and questionable time management

*If you enjoyed this, consider giving it a ⭐!  It won't help my grades, but it'll make me feel better about my choices.*

**Happy New Year! 🎆**

</div>
