fn main() {
    let nums = Vec::from([1, 2, 3, 4, 5]);
    let arr = NumArray::new(nums);
    let res = arr.sum_range(0, 4);
    println!("{}", res);
}

#[derive(Debug)]
struct NumArray {
    nums: Vec<i32>,
}


/**
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl NumArray {
    fn new(nums: Vec<i32>) -> Self {
        Self { nums }
    }

    fn sum_range(&self, left: i32, right: i32) -> i32 {
        let mut total = 0;
        let start = left as usize;
        let end = (right + 1) as usize;

        for i in start..end {
            total += self.nums[i];
        }

        total
    }
}