#include <fstream>
#include <iostream>
#include <string>
using namespace std;

// Different OSs use different CLI commands to run Python
#ifdef _WIN32
// If your Windows machine runs Python in CLI with "python" instead of "py", update this line.
const string python = "py";
#else
// If your Mac/Linux machine runs Python in CLI with "python3" instead of "python", update this line.
const string python = "python3";
#endif

string game_difficulty = "easy";

/*
 * Prompts the user a number of gears.
 * Allows the user to enter an integer value between 3 and 8.
 * Will repear until valid input
 */
int get_num_gears() {
    cout << "Enter a number of gears between 3 and 7 inclusive";
    int num_gears;

    while (true) {
        cin >> num_gears;
        if (cin.fail() || cin.peek() != '\n' || num_gears < 3 || num_gears > 7) {
            cout << "Invalid input. Enter a number: " << endl;
            cin.clear();
            cin.ignore(numeric_limits<streamsize>::max(), '\n');
        } else {
            break;
        }
    }
    return num_gears;
}

int main() {
    // Welcome
    cout << "\n -------- Welcome to Rev Match! -------- \n" << endl;
    cout << "" << endl;
    // Get data
    int num_gears = get_num_gears();
    cin.clear();
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    // Print info to the console
    cout << "\nProcessing...\n\nYour interactive " << num_gears << " speed gearbox will begin soon. This may take a few seconds.\n" << endl;
    
    // Go to Python
    string command = python + " gearbox.py " + to_string(num_gears);
    system(command.c_str());
    return 0;
}
