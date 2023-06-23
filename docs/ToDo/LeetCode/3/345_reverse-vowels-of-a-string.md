/*Question:
Write a function that takes a string as input and reverse only the vowels of a string.
*/

/*Input: "hello"
Output: "holle"*/

Java.version1:
class Solution {
    public String reverseVowels(String s) {
        
        int start = 0;
        
        char[] res = s.toCharArray();
        int length_of_string = res.length;
        int last = length_of_string - 1;
        while(start<last){
            while(res[start]!='a'&&res[start]!='e'&&res[start]!='i'&&res[start]!='o'&&res[start]!='u'&&res[start]!='A'&&res[start]!='E'&&res[start]!='I'&&res[start]!='O'&&res[start]!='U'&&start<length_of_string&&start<last){
                start++;
            }
            while(res[last]!='a'&&res[last]!='e'&&res[last]!='i'&&res[last]!='u'&&res[last]!='o'&&last>=0&&res[last]!='A'&&res[last]!='E'&&res[last]!='I'&&res[last]!='U'&&res[last]!='O'&&last>=0&&last>start){
                last--;
            }
            if(start>=last)
            break;
            else if(res[start]!= res[last]){
                char temp = res[start];
                res[start] = res[last];
                res[last] = temp;
                
            }
            start++;
            last--;
        }
        return new String(res);

    }
}
