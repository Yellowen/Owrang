---
{
	"_label": "Sales Invoice"
}
---
A Sales Invoice is a bill that you send to your Customers, against which they will process your payment. 

If you have managed to create Sales Orders or Delivery Notes, creating a Sales Invoice follows the same process. 

You can create a Sales Invoice directly from

> Accounting > Sales Invoice > New Sales Invoice

or from the “Make Sales Invoice” button in the Sales Order or Delivery Note.



<br>


![Sales Invoice](img/sales-invoice.png)

<br>




#### Accounting Impact

All Sales must be booked against an “Income Account”. This refers to an Account in the “Income” section of your Chart of Accounts. It is a good practice to classify your income by type (like product income, service income etc). The Income Account must be set for each row of the Items table.

> Tip: To set default Income Accounts for Items, you can set it in the Item or Item Group.

The other account that is affected is the Account of the Customer. That is automatically set from “Debit To” in the heading section.

You must also mention the Cost Centers in which your Income must be booked. Remember that your Cost Centers tell you the profitability of the different lines of business or product. You can also set a default Cost Center in the Item master.

#### Accounting entries (GL Entry) for a typical double entry “Sale”:

When booking a sale (accrual):

**Debit:** Customer (grand total)
**Credit:** Income (net total, minus taxes for each Item) 
**Credit:** Taxes (liabilities to be paid to the government)

> To see entries in your Sales Invoice after you “Submit”, click on “View Ledger”.

#### Dates

Posting Date: The date on which the Sales Invoice will affect your books of accounts i.e. your General Ledger. This will affect all your balances in that accounting period. 

Due Date: The date on which the payment is due (if you have sold on credit). This can be automatically set from the Customer master.

#### Recurring Invoices

If you have a contract with a Customer where you bill the Customer on a monthly, quarterly, half-yearly or annual basis, you can check the “Recurring Invoice” box. Here you can fill in the details of how frequently you want to bill this Invoice and the period for which the contract is valid.

Owrang will automatically create new Invoices and mail it to the email ids you set.

---

#### "Pro Forma" Invoice

If you want to give an Invoice to a Customer to make a payment before you deliver, i.e. you operate on a payment first basis, you should create a Quotation and title it as a “Pro-forma Invoice” (or something similar) using the Print Heading feature. 

“Pro Forma” means for formality. Why do this? Because if you book a Sales Invoice it will show up in your “Accounts Receivable” and “Income”. This is not ideal as your Customer may or may not decide to pay up. But since your Customer wants an “Invoice”, you could give the Customer a Quotation (in Owrang) titled as “Pro Forma Invoice”. This way everyone is happy.

This is a fairly common practice. We follow this at Web Notes too.
