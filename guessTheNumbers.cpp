#include <iostream>
#include <ctime>
#include <vector>
#include <stack>
using namespace std;

class Game {
private:
    int secretNumber;
    int maxGuesses;
    int remainingGuesses;
    vector<int> guesses;
    stack<int> guessedNumbers;

public:
    Game(int maxGuesses) {
        this->maxGuesses = maxGuesses;
        remainingGuesses = maxGuesses;
        srand(time(NULL));
        secretNumber = rand() % 100 + 1;
    }

    bool isGuessValid(int guess) {
        return guess >= 1 && guess <= 100;
    }

    void makeGuess(int guess) {
        guesses.push_back(guess);
        guessedNumbers.push(guess);
        remainingGuesses--;

        if (guess == secretNumber) {
            cout << "Selamat! Tebakanmu benar. Angka yang dicari adalah " << secretNumber << endl;
        } else if (guess < secretNumber) {
            cout << "Tebakanmu terlalu kecil!" << endl;
        } else {
            cout << "Tebakanmu terlalu besar!" << endl;
        }

        if (remainingGuesses == 0) {
            cout << "Maaf, kesempatanmu telah habis. Angka yang dicari adalah " << secretNumber << endl;
        }
    }

    int getRemainingGuesses() {
        return remainingGuesses;
    }

    vector<int> getGuesses() {
        return guesses;
    }

    stack<int> getGuessedNumbers() {
        return guessedNumbers;
    }
};

int main() {
    int maxGuesses = 5;
    Game game(maxGuesses);

    cout << "Selamat datang di Game Tebak Angka!" << endl;
    cout << "Saya telah memilih sebuah angka antara 1 hingga 100." << endl;
    cout << "Kamu memiliki " << maxGuesses << " kesempatan untuk menebak." << endl;

    while (game.getRemainingGuesses() > 0) {
        int guess;
        cout << "Tebak angka: ";
        cin >> guess;

        if (!game.isGuessValid(guess)) {
            cout << "Tebakan tidak valid. Masukkan angka antara 1 hingga 100." << endl;
            continue;
        }

        game.makeGuess(guess);

        if (game.getRemainingGuesses() > 0) {
            cout << "Kamu memiliki " << game.getRemainingGuesses() << " kesempatan tersisa." << endl;
        }
    }

    vector<int> guesses = game.getGuesses();
    cout << endl << "Riwayat tebakan:" << endl;
    for (int guess : guesses) {
        cout << guess << " ";
    }
    cout << endl;

    stack<int> guessedNumbers = game.getGuessedNumbers();
    cout << "Angka-angka yang ditebak (dari akhir):" << endl;
    while (!guessedNumbers.empty()) {
        cout << guessedNumbers.top() << " ";
        guessedNumbers.pop();
    }
    cout << endl;

    return 0;
}
