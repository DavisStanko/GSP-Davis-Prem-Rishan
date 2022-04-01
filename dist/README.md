# GSP-Davis-Prem-Rishan

This program was made to translate text to and from languages of your choosing.

## Getting Started

### Prerequisites

Please be sure to install the following before running the program.

- Python 3.x
- Tkinter
- Tkinter.ttk
- gTTS
- deep_translator
- playsound
- sqlite3
- datetime
- PyAudio
- Portaudio

## Usage

- Start the program by executing the main.py file.
- Input the text to be translated in the designated field.
  - The language will be detected automatically.
- Select the output language from the drop down menu.
- Click the submit button when ready.

The translated text will be simultaneously displayed and spoken.

When possible, the program will speak the text with a language appropriate accent. This is not supported for all languages.

To display the program in light mode, click the appearance toggle at the top right corner.

## Compatibility

Some operating systems modify Tkinter's styling.

- Linux and BSD should not modify the styling at all and as such are the recommended operating systems for this project.
- MacOS adds a thin border around buttons but the GUI is otherwise unchanged.
- Windows messes up Text and Label boxes sizing, as well as making the list non-scrollable.

## Authors

- **Davis Stanko** - [Website](https://davisstanko.com)

- **Prem Patel**

- **Rishan Subagar**

## License

This project is licensed under the [GPL-3.0](LICENSE.md) GNU General Public License - see the [LICENSE.md](LICENSE.md) file for details
