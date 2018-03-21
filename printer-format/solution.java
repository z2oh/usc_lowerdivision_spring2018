import java.util.Scanner;
import java.util.Arrays;
public class solution
{
	public static void main(String[] args)
	{
		Scanner sc = new Scanner(System.in);

		int[] nums = Arrays.stream(sc.nextLine().split(" "))
		.mapToInt(Integer::parseInt)
		.toArray();
		System.out.print(nums[0]);
		for(int i=2; i < nums.length; i++)
		{
			System.out.print("-" + (nums[i]-1) + "," + (nums[i]+1));
		}//prints valid format
		System.out.println("-" + nums[1]);
	}
}
