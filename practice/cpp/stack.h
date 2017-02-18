struct stacknode
{

stacknode* upper;
	stacknode* lower;
	(void*) data; // must be cast
}

class Stack
{
	public:
		push(void* data);
		pop(void);
		peek(void);
	private:
		stacknode* current;
		
}

