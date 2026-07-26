public class Lasagna {

	public int expectedMinutesInOven() {
		return 40;
	}

	public int remainingMinutesInOver(int minutes) {
		return expectedMinutesInOven() - minutes;

	}

    // TODO: define the 'preparationTimeInMinutes()' method

	public int preparationTimeInMinutes(int layers) {
		return expectedMinutesInOven() + (2 * layers);
	}

    // TODO: define the 'totalTimeInMinutes()' method

	public int totalTimeInMinutes(int layers, int minutes) {
		return preparationTimeInMinutes(layers) - minutes;
	}

}
