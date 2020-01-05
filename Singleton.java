/**
A single is a design pattern in which a class has only one instance.
Resources: https://www.techopedia.com/definition/15830/singleton
https://github.com/SuyashLakhotia/TechInterview/blob/master/4%20-%20Design%20Patterns.md
**/
public Singleton{
	private static Singleton instance = null;
	private Singleton(){ 
		//constructor
	}
	public static Singleton getInstance(){
		if(instance == null){
			instance = new Singleton();
		}
		return instance;
	}
}