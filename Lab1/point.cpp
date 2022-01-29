#include <iostream>

using namespace std;

const int M = 5;
const int N = 2;

int findMax(int *a) {
    int i;
    int max = a[0];
    for (i = 1; i < M; i++)
        if (a[i] > max)
            max = a[i];
            
    return max;
}

int* getDistances(int a[][N]) {
    int *distances = new int(M);
  
    int i, j;
    for (i = 0; i < M; i++)
      distances[i] = abs(a[i][0] - a[i][1]);
      
    return distances;
}

int main() {
    int points[M][N] = {{7, 3}, {4, 6}, {7, 8}, {4, 1}, {6, 6}};
    
    int* distances = getDistances(points);
    
    cout << "Max distance: " << findMax(distances) << endl;

    return 0;
}

