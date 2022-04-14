# Testing

**Testing done on non-mac machines should ignore minor front end issues.**

## Checks

- **GUI displays**
  - Dark mode/ Light mode
    - Also affects child windows
- Options
  - Speech output
  - Turn on switch using "Enable Speech"
  - Help menu displays
    - Scrollbar works
- Input
  - **Typing input**
    - Text selection
      - Cut, copy, paste, etc
    - Text wraps
  - Speech input (if on)
- Input translated
  - **Text output**
    - Text wraps
  - Speech file written (if on)
  - Speech output (if on)
    - Right accent if applicable
- Copy button works
- History written to SQL DB
  - Treeview GUI displays
    - Copy input
    - Copy output
