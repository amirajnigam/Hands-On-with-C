int firstUniqChar(char * s)
{
	    int A[26] = {0};
	        
	        int i,len;
		    len = strlen(s);
		        
		        for( i = 0; i < len; ++i)
				        A[s[i] - 'a']++;  // incrementing the occurance te repeating character 
			    for( i = 0; i < len; ++i)
				        {
						        if(A[s[i] - 'a'] == 1)
								            return(i);
							    }
			        return (-1);
}


//s[i] = "loveleetcode"
////A[s[i] -'a']         count      letter count 
////A['l' - 'a'] = 11    A[11]++    l = 1
////A['o' - 'a'] = 14    A[14]++    o = 1
////A['v' - 'a'] = 21    A[21]++    v = 1
////A['e' - 'a'] = 5     A[5]++     e = 1
////A['l' - 'a'] = 11    A[11]++    l = 2
////A['e' - 'a'] = 5     A[5]++     e = 2
////A['e' - 'a'] = 5     A[5]++     e = 3
////A['t' - 'a'] = 19    A[19]++    t = 1
////A['c' - 'a'] = 2     A[1]++     c = 1
////A['o' - 'a'] = 14    A[14]++    o = 2
////A['d' - 'a'] = 3     A[3]++     d = 1
////A['e' - 'a'] = 5     A[5]++     e = 4
//
////l = 2
////o = 2
////v = 1
////e = 3
////t = 1
////c = 1
////d = 1
