export function lastWordLength(given: string): number{
    let indefiniteWhitespace: RegExp = /[\W]+/
    let clean_input = given.trim()
    let words: string[] = clean_input.split(indefiniteWhitespace)
    return words[words.length-1].length
}