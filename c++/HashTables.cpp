/*
    HashTables
    Hashing is a technique that is used to uniquely identify a specific object from a group of similar objects
    Using Separate chaining method to remove collisions
    Source: https://www.hackerearth.com/practice/data-structures/hash-tables/basics-of-hash-tables/tutorial/
*/
#include<bits/stdc++.h>
#define max(a,b) (a)>(b)?(a):(b)
#define min(a,b) (a)<(b)?(a):(b)
#define abs(a)   (a)<0 ? -(a) : (a)
#define MOD 1e9 + 7
#define MAXN 65536
#define MAXLG 17
#define Char_To_Ind(a,b) (int)(a) - (int)(b)
static const int INF = 0x3f3f3f3f;
static const long long INFL = 0x3f3f3f3f3f3f3f3fLL;
using namespace std;

class Node {
    string data;
    int count = 0;
    Node *next;
    public:
        Node(string x) {
            data = x;
            count += 1;
            next = NULL;
        }
        string getData() {
            return data;
        }
        void setNextNode(Node *newNode) {
            next = newNode;
        }
        Node *getNextNode() {
            return next;
        }
        void incrementCount() {
            count += 1;
        }
        void decrementCount() {
            count -= 1;
            count = count < 0 ? 0 : count;
        }
        int getCount() {
            return count;
        }
};

class LinkedList {
    Node *head = NULL;
    public:
        Node* getNodeWithGivenData(string data) {
            Node *ptr = head;
            while(ptr && ptr->getData() != data && ptr->getNextNode() != NULL) {
                ptr = ptr->getNextNode();
            }
            return ptr;
        }
        void findOrInsertNode(string data) {
            Node *newNode = new Node(data);
            if (head == NULL) {
                head = newNode;
            } else {
                Node* nodeWithGivenData = getNodeWithGivenData(data);
                if (nodeWithGivenData -> getData() == data) {
                    nodeWithGivenData->incrementCount();
                } else {
                    nodeWithGivenData->setNextNode(newNode);
                }
            }
        }
        void removeGivenNode(string data) {
            Node *ptr = head;
            if (head && head->getData() == data) {
                head = head->getNextNode();
            } else {
                while(ptr && ptr->getNextNode() && ptr->getNextNode()->getData() != data) {
                    ptr = ptr->getNextNode();
                }
                if (ptr && ptr->getNextNode()) {
                    Node *temp = ptr->getNextNode();
                    ptr->setNextNode(temp->getNextNode());
                    temp->setNextNode(NULL);
                }
            }
        }
        void decrementCountOfGivenNode(string data) {
            Node * ptr = getNodeWithGivenData(data);
            if (ptr->getData() == data) {
                ptr->decrementCount();
                if (!ptr->getCount()) {
                    removeGivenNode(data);
                }
            }
        }
        void printLinkedList() {
            Node *ptr = head;
            while(ptr) {
                cout<<ptr->getData()<<":"<<ptr->getCount()<< " -> ";
                ptr = ptr->getNextNode();
            }
            cout<<"NULL\n";
        }
};

class HashTable {
    vector<LinkedList*> hm;
    int primeNumber;
    int capacity;
    public:
        HashTable(int pN, int c) {
            primeNumber = pN ;
            capacity = c;
            hm.resize(capacity, NULL);
        }
        int getIndex(string data) {
            int sum = 0;
            for (int i = 0; i < data.length(); i++) {
                sum += (int(data[i]) * 10 + (i + 1));
            }
            return (sum % primeNumber) % capacity;
        }
        void insertKey(string data) {
            int index = getIndex(data);
            // cout<<data<<" "<<index<<"\n";
            if (!hm[index]) {
                hm[index] = new LinkedList();
            }
            hm[index]->findOrInsertNode(data);
        }
        void removeKey(string data) {
            int index = getIndex(data);
            hm[index]->decrementCountOfGivenNode(data);
        }
        void printHashMap() {
            for (int i = 0; i < capacity; i++) {
                if (!hm[i]) {continue;}
                cout<<i<<" ";
                hm[i]->printLinkedList();
            }
        }
};

void solve() {
    HashTable *hashMap = new HashTable(2069, 20);
    hashMap->insertKey("abcdef");
    hashMap->insertKey("bcdfea");
    hashMap->insertKey("cdefab");
    hashMap->insertKey("defabc");
    hashMap->insertKey("this");
    hashMap->printHashMap();
    hashMap->removeKey("this");
    hashMap->insertKey("abcdef");
    hashMap->printHashMap();
    hashMap->removeKey("abcdef");
    hashMap->printHashMap();
}
int main() {
    solve();
}