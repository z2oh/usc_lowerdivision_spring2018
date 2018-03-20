import java.util.Scanner;
public class printerFormat
{
	public static void main(String[] args)
	{
		Scanner scn = new Scanner(System.in);
		String input = scn.nextLine();

		String[] str_nums = input.split(" ");
		int[] nums = new int[str_nums.length];

		int i = 0;
		for (String s_num : str_nums)
		{
			nums[i++] = Integer.parseInt(s_num); 
		}//places numbers in array
	
		System.out.print(nums[0]);
		for(i=2; i < nums.length; i++)
		{
			System.out.print("-" + (nums[i]-1) + "," + (nums[i]+1));
		}//prints valid format
		System.out.println("-" + nums[1]);
	}
}
