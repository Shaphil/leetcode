fn main() {
    let nums = Vec::from([1, 2, 3, 4, 5]);
    let arr = NumArray::new(nums);
    let res = arr.sum_range(0, 4);
    println!("{}", res);
}

#[derive(Debug)]
struct NumArray {
    prefix_sum: Vec<i32>,
}

impl NumArray {
    fn new(nums: Vec<i32>) -> Self {
        let mut prefix_sum = vec![0; nums.len() + 1];
        for i in 0..nums.len() {
            prefix_sum[i + 1] = prefix_sum[i] + nums[i];
        }
        Self { prefix_sum }
    }

    fn sum_range(&self, left: i32, right: i32) -> i32 {
        let start = left as usize;
        let end = (right + 1) as usize;
        self.prefix_sum[end] - self.prefix_sum[start]
    }
}