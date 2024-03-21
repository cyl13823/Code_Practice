#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define TABLE_SIZE 10

struct Node {
    int key;
    int value;
    struct Node* next;
};

struct HashTable {
    struct Node* table[TABLE_SIZE];
};

int hashFunction(int key) {
    return key % TABLE_SIZE;
}

struct Node* createNode(int key, int value) {
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    newNode->key = key;
    newNode->value = value;
    newNode->next = NULL;
    return newNode;
}

void insert(struct HashTable* ht, int key, int value) {
    int index = hashFunction(key);
    struct Node* newNode = createNode(key, value);

    // If no element present at index
    if (ht->table[index] == NULL) {
        ht->table[index] = newNode;
    } else {
        // Collision handling by chaining
        struct Node* temp = ht->table[index];
        while (temp->next != NULL) {
            temp = temp->next;
        }
        temp->next = newNode;
    }
}

int search(struct HashTable* ht, int key) {
    int index = hashFunction(key);
    struct Node* temp = ht->table[index];

    while (temp != NULL) {
        if (temp->key == key) {
            return temp->value;
        }
        temp = temp->next;
    }
    return -1; // Element not found
}

int main() {
    struct HashTable ht;
    memset(&ht, 0, sizeof(ht));

    // Insert elements into the hash table
    insert(&ht, 1, 10);
    insert(&ht, 2, 20);
    insert(&ht, 3, 30);

    // Search for elements in the hash table
    printf("Value for key 1: %d\n", search(&ht, 1));
    printf("Value for key 2: %d\n", search(&ht, 2));
    printf("Value for key 3: %d\n", search(&ht, 3));
    printf("Value for key 4: %d\n", search(&ht, 4)); // Not present

    return 0;
}