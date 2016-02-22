package edu.iu.clrs.sort;

import java.util.Arrays;
import java.util.Scanner;
import java.util.concurrent.ThreadLocalRandom;

/**
 * The Class RandomizedQuicksort.
 * 
 * @author Gourav Shenoy
 */
public class RandomizedQuickSort {

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
	public RandomizedQuickSort(int arraySize) {
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
	 * Partition prime.
	 * 
	 * @param begin
	 *            the begin
	 * @param end
	 *            the end
	 * @return the int[]
	 */
	public int[] partitionPrime(int begin, int end) {

		int x = this.getIntArray()[end];
		int i = begin - 1, t = i + 1;

		// Permute elements < pivot, to the left.
		for (int j = begin; j <= (end - 1); j++) {
			if (this.getIntArray()[j] < x) {
				this.swapArrayElements(i + 1, j);
				i++;
			}
		}

		// Push elements == pivot, to the center.
		for (t = (i + 1); t < end && this.getIntArray()[t] == x; t++)
			;

		// Move the elements == pivot, towards right to center.
		for (int k = end; k >= t; k--) {
			if (this.getIntArray()[k] == x) {
				this.swapArrayElements(t, k);
				t++;
			}
		}

		// Return array of values with p and t.
		int[] pivotArray = new int[2];

		pivotArray[0] = (i + 1);
		pivotArray[1] = (t - 1);

		return pivotArray;
	}

	/**
	 * Quick sort prime.
	 * 
	 * @param begin
	 *            the begin
	 * @param end
	 *            the end
	 */
	public void quickSortPrime(int begin, int end) {
		if (begin < end) {
			int partition = this.randomizedPartition(begin, end);
			this.quickSortPrime(begin, partition - 1);
			this.quickSortPrime(partition + 1, end);
		}
	}

	/**
	 * Randomized quick sort prime.
	 * 
	 * @param begin
	 *            the begin
	 * @param end
	 *            the end
	 */
	public void randomizedQuickSortPrime(int begin, int end) {
		if (begin < end) {
			int partitionArray[] = this.partitionPrime(begin, end);
			this.randomizedQuickSortPrime(begin, partitionArray[0] - 1);
			this.randomizedQuickSortPrime(partitionArray[1] + 1, end);
		}
	}

	/**
	 * The main method.
	 * 
	 * @param args
	 *            the arguments
	 */
	public static void main(String[] args) {

		Scanner scanner = new Scanner(System.in);

		try {
			/* Input size of array */
			System.out.print("Enter the length of input array: ");
			int length = scanner.nextInt();

			/* Build array filled with random int */
			RandomizedQuickSort rqSort = new RandomizedQuickSort(length);
			System.out.println("Array of Size {" + length
					+ "} (Before Sorting) :: ");
			/* Print array before sort */
			rqSort.printIntArray();

			/* Function call to randomizedQuickSortPrime */
			rqSort.randomizedQuickSortPrime(0, length - 1);

			/*
			 * UNCOMMENT TO RUN... DONT FORGET TO COMMENT CALL TO
			 * RANDOMIZEDQUICKSORTPRIME ABOVE ELSE ARRAY WILL BE SORTED TWICE
			 */
			/* Function call to quickSortPrime */
			// rqSort.quickSortPrime(0, length - 1);

			System.out.println("Array of size {" + length
					+ "} (After Sorting) :: ");

			/* Print array after sort */
			rqSort.printIntArray();
		} catch (Exception ex) {
			ex.printStackTrace();
		} finally {
			scanner.close();
		}
	}

}
