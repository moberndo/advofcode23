using aoc2024.Days;

namespace aoc2024;

internal class Program
{
    static void Main(string[] args)
    {
        //Run<Day01>();
        //Run<Day02>();
        Run<Day03>();
    }

    private static void Run<T>()
        where T : IDay, new() => new T().Run();
}
