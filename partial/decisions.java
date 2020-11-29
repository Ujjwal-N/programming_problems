
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.HashSet;
import java.util.Set;

public class decisions {
	Node head;
	int levels;
	boolean[] values;
	int index;
	public static void main(String[] args) {
    	
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		try {
			int levels = Integer.parseInt(br.readLine());
	    	String raw = br.readLine();
	    	
	    	String[] splitted = raw.split(" ");
	    	boolean[] values = new boolean[splitted.length];
	    	for(int i = 0; i < splitted.length; i++) {
	    		if(splitted[i].equals("0")) {
	    			values[i] = false;
	    		}else {
	    			values[i] = true;
	    		}
	    	}
	    	
	    	Tree bdTree = new Tree(levels, values);
			
		}catch(IOException e) {
			
		}

    	
    	
    }
    public Tree(int levels, boolean[] values) {
    	this.levels = levels;
    	this.values = values;
    	this.index = 0;
    	head = constructTree(0);
    	optimizeTree();
    	
    	System.out.println(countNodes());
    	//System.out.println(this);
    }
	private Node constructTree(int level) {
		Node retNode = new Node();
		if(level == levels) {
			retNode.isLeafNode = true;
			retNode.value = values[index];
			retNode.level = level;
			//System.out.println("leaf node created with " + index);
			index++;
			return retNode;
		}

		Node left = constructTree(level + 1);
		Node right = constructTree(level + 1);
		retNode.left = left;
		retNode.right = right;
		retNode.isLeafNode = false;
		retNode.level = level;
		//System.out.println("node created at " + level);
		return retNode;
		
	}

	

	private void optimizeTree() {
		recurseOptimize(head);
		fixLevels(head, 0);
		linearOptimize();
	}
	private void recurseOptimize(Node currentNode) {
		if(currentNode.left.isLeafNode) {
			if(currentNode.left.value == currentNode.right.value) {
				
				currentNode.value = currentNode.left.value;
				currentNode.left = null;
				currentNode.right = null;
				currentNode.isLeafNode = true;
			}
			return;
		}
		recurseOptimize(currentNode.left);
		recurseOptimize(currentNode.right);
		
		if(currentNode.left.equals(currentNode.right)) {
			if(currentNode.left.isLeafNode) {
				currentNode.value = currentNode.left.value;
				currentNode.left = null;
				currentNode.right = null;
				currentNode.isLeafNode = true;
				return;
			}else {
				currentNode.right = currentNode.left;
			}
		}

	}
	HashSet<Node> newSet = new HashSet<Node>();
	private void linearOptimize() {
		newSet = new HashSet<Node>();
		newSet.add(head);
		recurseCheck(head);
	}
	private void recurseCheck(Node current) {
		if(current.left == null && current.right == null) {
			return;
		}
		if(newSet.contains(current.left)) {
			for(Node n : newSet) {
				if(n.equals(current.left)) {
					current.left = n;
				}
			}
			return;
		}else if(newSet.contains(current.right)){
			//System.out.println("here");
			for(Node n : newSet) {
				if(n.equals(current.right)) {
					current.right = n;
				}
			}
			return;
		}else {
			newSet.add(current.left);
			newSet.add(current.right);
			recurseCheck(current.left);
			recurseCheck(current.right);
		}

		
	}
	
	
	@Override
	public String toString() {

		StringBuffer retVal = new StringBuffer();
		recurseString(head, retVal, 0);
		return retVal.toString();
	}
	public void recurseString(Node current, StringBuffer retVal , int level) {
		
		if(current.isLeafNode) {
			retVal.append(current.value);
		}else {
			retVal.append("Level " + level);
			recurseString(current.left, retVal, level + 1);
			recurseString(current.right, retVal, level + 1);
		}

		
	}
	public void fixLevels(Node current, int level) {
		current.level = level;
		if(!current.isLeafNode) {
			fixLevels(current.left, level + 1);
			fixLevels(current.right, level + 1);
		}
	}
	
	
	private int countNodes() {
		nodesSet = new HashSet<Node>();
		nodesSet.add(head);
		recursePopulate(head);
		return nodesSet.size();
	}
	HashSet<Node> nodesSet = new HashSet<Node>();
	private void recursePopulate(Node current) {
		if(current.isLeafNode) {
			//nodesSet.add(current);
		}else {
			nodesSet.add(current.left);
			recursePopulate(current.left);
			if(!current.left.equals(current.right)) {
				nodesSet.add(current.right);
				recursePopulate(current.right);
			}
			
		}
	}
	
	public class Node implements Comparable{
		Node left;
		Node right;
		Boolean isLeafNode;
		Boolean value;
		int level;
		@Override
		public int compareTo(Object o) {
			Node that = (Node) o;
			if(this.obtainLeafValues().equals(that.obtainLeafValues()) && this.obtainLeafValues().size() > 1) {
				System.out.println("here");
				System.out.println(this.level == that.level);
				
				
			}
			if(this.level == that.level) {
				System.out.println(this.obtainLeafValues().equals(that.obtainLeafValues()) ? 0 : -1);
				return this.obtainLeafValues().equals(that.obtainLeafValues()) ? 0 : -1;
			}
			return this.level > that.level ? 1 : -1;
		}
		
		@Override
		public boolean equals(Object o) {
			Node that = (Node) o;
			ArrayList<Boolean> leafVals = this.obtainLeafValues();
			ArrayList<Boolean> otherLeafVals = that.obtainLeafValues();
			
			if(leafVals.size() != otherLeafVals.size()) {
				return false;
			}
			for(int i = 0; i < leafVals.size(); i++) {
				if(otherLeafVals.get(i) != leafVals.get(i)) {
					return false;
				}
			}
			
			return this.level == that.level;
			
			

		}
		
		public ArrayList<Boolean> obtainLeafValues() {
			ArrayList<Boolean> retVal = new ArrayList<Boolean>();
			recurseAdd(retVal, this);
			return retVal;
		}
		private void recurseAdd(ArrayList<Boolean> currentVal, Node currentNode) {
			if(currentNode == null) {
				return;
			}
			if(currentNode.isLeafNode) {
				currentVal.add(currentNode.value);
				return;
			}
			recurseAdd(currentVal, currentNode.left);
			recurseAdd(currentVal, currentNode.right);
			 
		}
		
		@Override
		public int hashCode() {
			return level * this.obtainLeafValues().size();
		}

	}
}
