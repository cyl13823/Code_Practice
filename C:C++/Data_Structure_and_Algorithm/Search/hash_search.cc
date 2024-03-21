#include <iostream>
#include <vector>
using namespace std;

#define TABLE_SIZE 10

struct Node {
    int key;
    int value;
    struct Node* next;
};

class HashTable {
private:
    vector<Node*> table;

public:
    HashTable() {
        table.resize(TABLE_SIZE, nullptr);
    }

    int hashFunction(int key) {
        return key % TABLE_SIZE;
    }

    Node* createNode(int key, int value) {
        Node* newNode = new Node();
        newNode->key = key;
        newNode->value = value;
        newNode->next = nullptr;
        return newNode;
    }

    void insert(int key, int value) {
        int index = hashFunction(key);
        Node* newNode = createNode(key, value);

        // If no element present at index
        if (table[index] == nullptr) {
            table[index] = newNode;
        } else {
            // Collision handling by chaining
            Node* temp = table[index];
            while (temp->next != nullptr) {
                temp = temp->next;
            }
            temp->next = newNode;
        }
    }

    int search(int key) {
        int index = hashFunction(key);
        Node* temp = table[index];

        while (temp != nullptr) {
            if (temp->key == key) {
                return temp->value;
            }
            temp = temp->next;
        }
        return -1; // Element not found
    }
};

int main() {
    HashTable ht;

    // Insert elements into the hash table
    ht.insert(1, 10);
    ht.insert(2, 20);
    ht.insert(3, 30);

    // Search for elements in the hash table
    cout << "Value for key 1: " << ht.search(1) << endl;
    cout << "Value for key 2: " << ht.search(2) << endl;
    cout << "Value for key 3: " << ht.search(3) << endl;
    cout << "Value for key 4: " << ht.search(4) << endl; // Not present

    return 0;
}