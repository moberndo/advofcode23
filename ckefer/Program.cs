using aoc2024.Days;

namespace aoc2024;

internal class Program
{
    static void Main(string[] args)
    {
        Run<Day01>();
    }

    private static void Run<T>()
        where T : IDay, new() => new T().Run();
}
