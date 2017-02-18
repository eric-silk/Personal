class Stack
{
    public:
	void push(void* data);
	void* pop(void);
	void* peek(void);
    private:
	int createNode(void* data);
	int deleteNode(void);
}
