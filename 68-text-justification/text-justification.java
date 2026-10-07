class Solution {
    public List<String> fullJustify(String[] words, int maxWidth) {

        List<String> result = new ArrayList<>();
        int i = 0;

        while (i < words.length) {

            int j = i;
            int lineLength = 0;

            
            while (j < words.length &&
                   lineLength + words[j].length() + (j - i) <= maxWidth) {

                lineLength += words[j].length();
                j++;
            }

            int numberOfWords = j - i;
            int spaces = maxWidth - lineLength;

            StringBuilder line = new StringBuilder();

            
            if (j == words.length || numberOfWords == 1) {

                for (int k = i; k < j; k++) {
                    line.append(words[k]);

                    if (k < j - 1) {
                        line.append(" ");
                    }
                }

                
                while (line.length() < maxWidth) {
                    line.append(" ");
                }

            } else {

                int gaps = numberOfWords - 1;
                int spacesPerGap = spaces / gaps;
                int extraSpaces = spaces % gaps;

                for (int k = i; k < j; k++) {

                    line.append(words[k]);

                    if (k < j - 1) {

                        int currentSpaces = spacesPerGap;

                        
                        if (extraSpaces > 0) {
                            currentSpaces++;
                            extraSpaces--;
                        }

                        for (int s = 0; s < currentSpaces; s++) {
                            line.append(" ");
                        }
                    }
                }
            }

            result.add(line.toString());
            i = j;
        }

        return result;
    }
}