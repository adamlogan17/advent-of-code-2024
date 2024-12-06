// C++ Program to Read a file line by line using getline
#include <fstream>
#include <iostream>
#include <string>
#include <sstream>


using namespace std;

int** read_file(string file_name)
{
    ifstream file(file_name);
    string line;

    // First pass: Count the number of rows
    int row_count = 0;

    if (file.is_open()) {
        while (getline(file, line)) {
            row_count++;
        }

        // Reset the file pointer for the second pass
        file.clear();
        file.seekg(0, ios::beg);

        // Allocate memory for the two columns
        int** columns = new int* [2];
        columns[0] = new int[row_count]; // Left column
        columns[1] = new int[row_count]; // Right column

        // Second pass: Read values into arrays
        int index = 0;
        while (getline(file, line)) {
            istringstream stream(line);
            string word;
            char delimiter = ' ';
            bool right = false;

            while (getline(stream, word, delimiter)) {
                if (!right) {
                    columns[0][index] = stoi(word);
                }
                else {
                    columns[1][index] = stoi(word);
                }
            }
            index += 1;
        }

        file.close();
        return columns;
    }
    else {
        cerr << "Unable to open file!" << endl;
        return nullptr;
    }
}

int main()
{
    int** columns = read_file("input.txt");

    int* right_col = columns[0];
    int* left_col = columns[1];

    for (int i = 0; sizeof(right_col); i++) {
        cout << right_col[i] << endl;
    }

    delete[] right_col;
    delete[] left_col;
    delete[] columns;

    return 0;
}

