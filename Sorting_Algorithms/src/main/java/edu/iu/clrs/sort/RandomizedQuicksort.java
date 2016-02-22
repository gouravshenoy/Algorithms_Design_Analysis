package edu.iu.clrs.sort;

import java.util.Arrays;
import java.util.concurrent.ThreadLocalRandom;

/**
 * The Class RandomizedQuicksort.
 * 
 * @author Gourav Shenoy
 */
public class RandomizedQuicksort {

	/** The int array. */
	private int[] intArray;

	/** The Constant MIN_RANGE. */
	private static final int MIN_RANGE = 100;

	/** The Constant MAX_RANGE. */
	private static final int MAX_RANGE = 500;

	/**
	 * Instantiates a new randomized quicksort.
	 * 
	 * @param arraySize
	 *            the array size
	 */
	public RandomizedQuicksort(int arraySize) {
		this.buildRandomArray(arraySize);
	}

	/**
	 * Gets the int array.
	 * 
	 * @return the int array
	 */
	public int[] getIntArray() {
		return intArray;
	}

	/**
	 * Sets the int array.
	 * 
	 * @param intArray
	 *            the new int array
	 */
	public void setIntArray(int[] intArray) {
		this.intArray = intArray;
	}

	/**
	 * Builds the random array.
	 * 
	 * @param arraySize
	 *            the array size
	 */
	public void buildRandomArray(int arraySize) {
		int[] randomArray = new int[arraySize];
		try {
			for (int i = 0; i < arraySize; i++) {
				randomArray[i] = ThreadLocalRandom.current().nextInt(MIN_RANGE,
						MAX_RANGE);
			}

			this.setIntArray(randomArray);
		} catch (Exception ex) {
			System.err.println("Error Building Random Int Array, Reason: "
					+ ex.getMessage());
		}
	}

	/**
	 * Swap array elements.
	 * 
	 * @param index1
	 *            the index1
	 * @param index2
	 *            the index2
	 */
	public final void swapArrayElements(int index1, int index2) {
		int temp = this.getIntArray()[index1];
		this.getIntArray()[index1] = this.getIntArray()[index2];
		this.getIntArray()[index2] = temp;
	}

	/**
	 * Prints the int array.
	 */
	public void printIntArray() {
		System.out.println(Arrays.toString(this.getIntArray()));
	}

	/**
	 * Partition.
	 * 
	 * @param begin
	 *            the begin
	 * @param end
	 *            the end
	 * @return the int
	 */
	public int partition(int begin, int end) {
		int pivot = this.getIntArray()[end];
		int i = begin - 1;

		for (int j = begin; j <= (end - 1); j++) {
			if (this.getIntArray()[j] <= pivot) {
				// swap array[j] <--> array[i+1]
				this.swapArrayElements(j, i + 1);
				i++;
			}
		}

		// swap array[end] <--> array[i+1]
		this.swapArrayElements(end, i + 1);
		return (i + 1);
	}

	/**
	 * Randomized partition.
	 * 
	 * @param begin
	 *            the begin
	 * @param end
	 *            the end
	 * @return the int
	 */
	public int randomizedPartition(int begin, int end) {
		int randomIndex = ThreadLocalRandom.current().nextInt(begin, end + 1);
		this.swapArrayElements(randomIndex, end);
		return this.partition(begin, end);
	}

	/**
	 * Quick sort.
	 * 
	 * @param begin
	 *            the begin
	 * @param end
	 *            the end
	 */
	public void randomizedQuickSort(int begin, int end) {
		if (begin < end) {
			int partition = this.randomizedPartition(begin, end);
			this.randomizedQuickSort(begin, partition - 1);
			this.randomizedQuickSort(partition + 1, end);
		}
	}

	/**
	 * The main method.
	 * 
	 * @param args
	 *            the arguments
	 */
	public static void main(String[] args) {
		RandomizedQuicksort sort = new RandomizedQuicksort(10);
		sort.printIntArray();
		sort.randomizedQuickSort(0, 9);
		sort.printIntArray();
	}

}
