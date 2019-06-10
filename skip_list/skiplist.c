// UFSC - Campus Trindade
// PPGEAS - Introducao a Algoritmos
// Matuzalem Muller dos Santos
// 2019/1
#include <stdio.h>
#include <stdlib.h>
#include <limits.h>
#include <time.h>
#define M_HEIGHT 10

// Node and skip list structures
typedef struct node {
    int key;
    int value;
    struct node **next;
} node;

static node *nil = NULL;

typedef struct skip_list {
    int height;
    int size;
    node *head;
} skiplist;

//------------------------------------------------------------------------------
// Starts skip list with head and tail
void init_skip_list(skiplist *s) {

    node *head = (node *) malloc(sizeof(node));
    s->head = head;
    s->head->key = INT_MIN;
    s->head->value = 0;
    s->head->next = (node **) calloc(M_HEIGHT , sizeof(node *));

    nil = (node *) malloc(sizeof(node));
    nil->key = INT_MAX;
    node *tail = nil;

    s->height = 1;
    s->size = 0;

    for (int i = 0; i < M_HEIGHT; i++) {
        s->head->next[i] = tail;
    }

    srand(time(NULL));
}

//------------------------------------------------------------------------------
// Calculates height from each node
int random_height () {
    int height = 1;
    
    while (height < M_HEIGHT) {
        if ((rand() % 2) == 1){
            height += 1;
        } else {
            break;
        }
    }
    return height;
}

//------------------------------------------------------------------------------
// Inserts node into skip list
int insert_node_in_skip(skiplist *s, int key, int value) {
    int n = 0;                                      // complexity
    node *update[M_HEIGHT];
    node *x = s->head;

    int new_height;

    for (int i = (s->height - 1); i >= 0; i--) {
        while (x->next[i]->key < key) {
            x = x->next[i];
        }
        update[i] = x;
        n++;
    }

    x = x->next[0];

    if (x->key == key) {
        x->value = value;
    } else {
        s->size += 1;
        new_height = random_height();
        
        if (new_height > s->height) {
            for (int i = s->height; i < new_height; i++) {
                update[i] = s->head;
                n++;
            }
            s->height = new_height;
        }

        x = (node *) malloc(sizeof(node));

        x->key = key;
        x->value = value;
        x->next = (node **) calloc(new_height, sizeof(node *));

        for (int i = 0; i < new_height; i++) {
            x->next[i] = update[i]->next[i];
            update[i]->next[i] = x;
        }
    }
    return n;
}

//------------------------------------------------------------------------------
// Deletes node from memory
void destroy_node(node *x) {
    if (x) {
        free(x->next);
        free(x);
    }
}

//------------------------------------------------------------------------------
// Remove node that has key value from skip list
int remove_from_skip(skiplist *s, int key) {
    int n = 0;                                  // complexity

    node *update[M_HEIGHT];
    node *x = s->head;

    for(int i=(s->height-1); i>=0; i--){
        while (x->next[i]->key < key) {
            x = x->next[i];
        }
        update[i] = x;
        n++;
    }

    x = x->next[0];
    if (x->key == key) {
        for (int i = 0; i < s->height; i++) {
            if (update[i]->next[i] != x) {
                break;
            }
            update[i]->next[i] = x->next[i];
            n++;
        }
        destroy_node(x);

        while (s->height > 1 && s->head->next[s->height - 1] == nil) {
            s->height -= 1;
        }

        s->size -= 1;
    }
    return n;
}

//------------------------------------------------------------------------------
// Searches for node in skip list
// Returns True if node is found, otherwise returns False
node *search(skiplist *s, int key) {
    
    node *x = s->head;

    for (int i = s->height - 1; i >= 0; i--) {
        while (x->next[i]->key < key) {
            x = x->next[i];
        }
    }
    
    x = x->next[0];

    if (x->key == key) {
        return x;
    } else {
        return NULL;
    }    
}

//------------------------------------------------------------------------------
// Prints skip list
void print_skip_list(skiplist *s) {
    node *x;

    // printf("Height: %d\n------------\n", s->height);

    for(int i = s->height-1; i >= 0; i--){
        x = s->head;

        while (x != NULL && x->next[i] != nil) {
            printf("%d ", x->next[i]->key);
            x = x->next[i];
        }

        if (x == NULL) {
            printf("NULL");
        }

        printf("\n");
    }
}

//------------------------------------------------------------------------------
// Tests insertion and deletion of values in skip list
void test_skip_list(int lenght){
    int array[lenght+10];   // Array is a bit longer so new values can be added
    int i, n = 0;
    int index;
    int percent_20;
    skiplist list;

    init_skip_list(&list);

    printf("---------------------------------------------------------------\n");
    for (i = 0; i < lenght; i++) {
        array[i] = rand() % 100;
        // printf("%d ", array_256[i]);
    }

    printf("\nInsert: n = %d\n", lenght);
    for (i = 0; i < lenght; i++) {
        n += insert_node_in_skip(&list, array[i], rand() % 10000);
    }
    printf("Number of steps taken to insert %d values: %d\n", lenght, n);

    n = insert_node_in_skip(&list, array[i], rand() % 10000);
    printf("Number of steps taken to insert an additional element: %d\n", n);

    percent_20 = lenght * 20 / 100;
    printf("\nDelete: n = %d\n", percent_20);
    for (n = 0, i = 0; i < percent_20; i++) {
        index = rand() % lenght;
        n += remove_from_skip(&list, array[index]);
        // printf("%d ", n);
    }
    printf("Number of steps taken to delete %d values: %d\n", percent_20, n);

    index = rand() % lenght;
    n = remove_from_skip(&list, array[index]);
    printf("Number of steps taken to delete an additional element: %d\n", n);
}

//------------------------------------------------------------------------------
int main(){

    test_skip_list(256);
    test_skip_list(4096);
    test_skip_list(65536);

    return 0;
}