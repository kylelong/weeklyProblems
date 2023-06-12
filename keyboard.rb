
def oneRow(words)
    words.select!{|w| w.match(/^[asdfghjkl]+$|^[zxcvbnm]+$|^[qwertyuiop]+$/)}
    words
end
p oneRow(['candy', 'fart', 'pop', 'Zelda', 'flag', 'typewriter']) #  ['pop', 'flag', 'typewriter']