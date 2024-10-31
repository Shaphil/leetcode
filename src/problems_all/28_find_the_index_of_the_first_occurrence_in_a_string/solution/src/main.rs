struct Solution {}

impl Solution {
    pub fn str_str(haystack: String, needle: String) -> i32 {
        let haystack_bytes = haystack.as_bytes();
        let needle_bytes = needle.as_bytes();
        let haystack_len = haystack_bytes.len();
        let needle_len = needle_bytes.len();

        if needle_len == 0 {
            return 0;
        }

        let mut i = 0;
        let mut j = 0;
        while i < haystack_len && j < needle_len {
            if haystack_bytes[i] == needle_bytes[j] {
                i += 1;
                j += 1;
            } else {
                i = i - j + 1;
                j = 0;
            }
        }

        if j == needle_len {
            (i - j) as i32
        } else {
            -1
        }
    }
}

fn main() {
    let haystack = "sadbutsad".to_string();
    let needle = "sad".to_string();

    let solution = Solution::str_str(haystack, needle);
    println!("{}", solution);
}