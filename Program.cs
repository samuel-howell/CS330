// See https://aka.ms/new-console-template for more information


printFIFO(new List<int>{345,123,874,692,475,105,376});
printSSTF(new List<int>{345,123,874,692,475,105,376});
printSCAN(new List<int>{345,123,874,692,475,105,376});
printCSCAN(new List<int>{345,123,874,692,475,105,376});

// FIFO
static void printFIFO(List<int> list)
{
    Console.WriteLine("FIFO: ");
    double sum = 0;
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
    Console.WriteLine("Number of Traversals {0}", sum);
    Console.WriteLine("Average Seek Length {0}", avg);
    Console.WriteLine("-------------------------------------------------");

}

// SSTF
static void printSSTF(List<int> list)
{
    Console.WriteLine("SSTF: ");
    double sum = 0;
    int[] a = list.ToArray();
    var firstElem = a[0];
    
    Array.Sort(a);

    //create a new list add everything above firstElem in order, then everything after first elem in order
    List<int> reformattedList = new List<int>{};
    reformattedList.Add(firstElem);  // add the firstelem as the start of the list
    foreach (var item in a)
    {
        if(item > firstElem)
        {
            reformattedList.Add(item);
        }
    }

    
    Array.Reverse(a); // have to reverse to the "higher" numbers below the firstelem come first

    foreach (var item in a)
    {
        if(item < firstElem)
        {
            reformattedList.Add(item);
        }
    }

    

    List<int> nta = new List<int>{}; // store next track accessed
    List<int> tt = new List<int>{}; // store track traversals

    while (reformattedList.Count != 1)        // seetting to one will prevent index out of bound on last tt entry
    {
        nta.Add(reformattedList[0]);
        tt.Add( Math.Abs(reformattedList[0] - reformattedList[1]) ); // get absolute val of the diff between the current selection and the next in the list
        
        reformattedList.RemoveAt(0);
    }

    Console.WriteLine("Next Track Accessed        Number of Tracks Traversed");
    for(int j = 0; j < nta.Count; j++)
    {
        Console.WriteLine("{0}                               {1}", nta[j], tt[j]);
        sum += tt[j];
    }
    double avg  = sum / tt.Count;

    Console.WriteLine("");
    Console.WriteLine("Number of Traversals {0}", sum);
    Console.WriteLine("Average Seek Length {0}", avg);
    Console.WriteLine("-------------------------------------------------");

}



static void printSCAN(List<int> list)
{
        Console.WriteLine("SCAN: ");
    double sum = 0;
    int[] a = list.ToArray();
    var firstElem = a[0];
    
    Array.Sort(a);
    Array.Reverse(a); // have to reverse to the "higher" numbers below the firstelem come first


    //create a new list add everything above firstElem in order, then everything after first elem in order
    List<int> reformattedList = new List<int>{};
    reformattedList.Add(firstElem);  // add the firstelem as the start of the list
    
      foreach (var item in a)
    {
        if(item < firstElem)
        {
            reformattedList.Add(item);
        }
    }
    
    reformattedList.Add(0); // add a zeroto signify hitting the innermost track
    Array.Reverse(a); // have to reverse to the "higher" numbers above the firstelem come first


    foreach (var item in a)
    {
        if(item > firstElem)
        {
            reformattedList.Add(item);
        }
    } 

    List<int> nta = new List<int>{}; // store next track accessed
    List<int> tt = new List<int>{}; // store track traversals

    while (reformattedList.Count != 1)        // seetting to one will prevent index out of bound on last tt entry
    {
        nta.Add(reformattedList[0]);
        tt.Add( Math.Abs(reformattedList[0] - reformattedList[1]) ); // get absolute val of the diff between the current selection and the next in the list
        
        reformattedList.RemoveAt(0);
    }

    Console.WriteLine("Next Track Accessed        Number of Tracks Traversed");
    for(int j = 0; j < nta.Count; j++)
    {
        Console.WriteLine("{0}                               {1}", nta[j], tt[j]);
        sum += tt[j];
    }
    double avg  = sum / tt.Count;

    Console.WriteLine("");
    Console.WriteLine("Number of Traversals {0}", sum);
    Console.WriteLine("Average Seek Length {0}", avg);
    Console.WriteLine("-------------------------------------------------");
}

static void printCSCAN(List<int> list)
{
        Console.WriteLine("CSCAN: ");
    double sum = 0;
    int[] a = list.ToArray();
    var firstElem = a[0];
    
    Array.Sort(a);
    Array.Reverse(a); // have to reverse to the "higher" numbers below the firstelem come first


    //create a new list add everything above firstElem in order, then everything after first elem in order
    List<int> reformattedList = new List<int>{};
    reformattedList.Add(firstElem);  // add the firstelem as the start of the list
    
      foreach (var item in a)
    {
        if(item < firstElem)
        {
            reformattedList.Add(item);
        }
    }
    
    reformattedList.Add(0); // add a zeroto signify hitting the innermost track
    reformattedList.Add(999); // add a zeroto signify hsnapping back



    foreach (var item in a)
    {
        if(item > firstElem)
        {
            reformattedList.Add(item);
        }
    } 

    List<int> nta = new List<int>{}; // store next track accessed
    List<int> tt = new List<int>{}; // store track traversals

    while (reformattedList.Count != 1)        // seetting to one will prevent index out of bound on last tt entry
    {
        nta.Add(reformattedList[0]);
        tt.Add( Math.Abs(reformattedList[0] - reformattedList[1]) ); // get absolute val of the diff between the current selection and the next in the list
        
        reformattedList.RemoveAt(0);
    }

    Console.WriteLine("Next Track Accessed        Number of Tracks Traversed");
    for(int j = 0; j < nta.Count; j++)
    {
        Console.WriteLine("{0}                               {1}", nta[j], tt[j]);
        sum += tt[j];
    }
    double avg  = sum / tt.Count;

    Console.WriteLine("");
    Console.WriteLine("Number of Traversals {0}", sum);
    Console.WriteLine("Average Seek Length {0}", avg);
    Console.WriteLine("-------------------------------------------------");
}
