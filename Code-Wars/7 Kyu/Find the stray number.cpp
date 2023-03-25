#include <bits/stdc++.h>
using namespace std;

int stray(vector<int> numbers) {
  sort(numbers.begin(), numbers.end());
  for (int i=0; i<numbers.size();i++) cout << numbers[i] << endl;
  int odd;
  if (numbers[0] != numbers[1]) odd = numbers[0];
  if (numbers[numbers.size()-1] != numbers[numbers.size()-2]) odd = numbers[numbers.size()-1];
  cout << odd;
  return odd;
};
