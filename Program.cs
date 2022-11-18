// See https://aka.ms/new-console-template for more information


var reqList = new List<int>{345,123,874,692,475,105,376};


printFIFO(reqList);

// FIFO
static void printFIFO(List<int> list)
{
    Console.WriteLine("FIFO: ");
    double sum = 0;
    int i = 0; // starting index
    List<int> a = list; //original list coming in
    List<int> nta = new List<int>{}; // store next track accessed
    List<int> tt = new List<int>{}; // store track traversals

    while (a.Count != 1)        // seetting to one will prevent index out of bound on last tt entry
    {
        nta.Add(a[0]);
        tt.Add( Math.Abs(a[0] - a[1]) ); // get absolute val of the diff between the current selection and the next in the list
        a.RemoveAt(0);            // remove first elem
    }

    Console.WriteLine("Next Track Accessed        Number of Tracks Traversed");
    for(int j = 0; j < nta.Count; j++)
    {
        Console.WriteLine("{0}                               {1}", nta[j], tt[j]);
        sum += tt[j];
    }
    double avg  = sum / tt.Count;

    Console.WriteLine("");
    Console.WriteLine("Average Seek Length {0}", avg);
    Console.WriteLine("-------------------------------------------------");

}