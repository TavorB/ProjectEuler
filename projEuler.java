public class projEuler {

	public static int calcp1() {
		int sum = 0;
		for(int i = 0; i < 1000; i++) {
			if (i % 3 == 0 || i % 5 == 0) {
				sum += i;
			}
		}
		return sum;
	}

	public static void main(String[] args) {
		System.out.println(calcp1());
	}
}