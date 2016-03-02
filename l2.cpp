struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode d = ListNode(0);
        int sum = 0;
        ListNode* current = &d;
        while(l1||l2){
        	if(l1){
        		sum+=l1->val;
        		l1=l1->next;
        	}
        	if(l2){
        		sum+=l2->val;
        		l2=l2->next;
        	}
        	current->next=new ListNode(sum%10);
        	sum/=10;
        	current=current->next;
        }
        if(sum==1){
        	current->next=new ListNode(1);
        }
        return d.next;
    }
};

