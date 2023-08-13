void reverseStringRecursive(char* s, int left, int right) {
    if (left >= right) {
        return;
    }
     
    char temp = s[left];
    s[left] = s[right];
    s[right] = temp;
    
    reverseStringRecursive(s, left + 1, right - 1);
}
void reverseString(char* s, int sSize)
{
    reverseStringRecursive(s, 0, sSize-1);           
}