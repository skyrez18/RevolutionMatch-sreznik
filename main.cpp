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


/*
* Pass a filename and determine if the file stream is in a good state
* https://cplusplus.com/reference/ios/ios/good/
*/
bool file_exists(const string& filename) {
    ifstream file(filename);
    return file.good();  
}

/*
 * Prompts the user for a filename.
 * Allows the user to enter nothing to use the default file (volvo850.txt).
 * If the file has extension .txt
 * and it exists in the project folder, return it.
 * Otherwise, return the default file
 */
string get_filename() {
    string filename;
    cout << "Enter a filename (.txt) with format as specified in README.md: " << endl;
    getline(cin, filename);
    // Go to defult image
    if (filename.empty()) {
        filename = "volvo850.txt";
        return filename;
    }
    if (file_exists(filename)) {
        // Check file extension with the thing Lisa taught me for my M2OEP project
        string extension = filename.substr(filename.find_last_of(".") + 1);
        if (extension == "txt") {
            return filename;
        }
    } else {
        cout << "File not found (or not .txt) using default file (1997 Volvo 850 Base)" << endl;
    }
    return "volvo850.txt";
}

int main() {
    // Welcome
    cout << "\n -------- Welcome to Rev Match! -------- \n" << endl;
    cout << "" << endl;
    string userfile = get_filename();
    ifstream filename(userfile);
    // Get gear count data
    string data; 
    int num_gears = 0;
    if(getline(filename, data)){
        num_gears = stoi(data);
    }

    // Print info to the console
    cout << "\nProcessing...\n\nYour interactive " << num_gears << " speed gearbox will begin soon. This may take a few seconds.\n" << endl;
    
    // Go to Python
    string command = python + " gearbox.py " + userfile;
    system(command.c_str());
    return 0;
}
