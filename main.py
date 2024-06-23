def read_log_file(filename):
    try:
        with open(filename, 'r') as file:
            return file.readlines()
    except FileNotFoundError:
        print(f'Error: File {filename} not found.')
    except IOError:
        print(f'Error: Unable to read file {filename}.')
    return []

def analyze_log(log_lines):
    events = []
    for line in log_lines[1:]:  
        timestamp, event, message = line.strip().split(',')
        events.append((timestamp, event, message))
    
    
    events.sort(reverse=True)
    
    issues = []
    for timestamp, event, message in events:
        print(f'{timestamp}: {event} - {message}')
        if 'explosion' in message.lower() or 'unstable' in message.lower():
            issues.append(f'{timestamp}: {event} - {message}')
    
    return issues

def save_issues(issues, filename):
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            for issue in issues:
                file.write(f'{issue}\n')
        print(f'Issues saved to {filename}')
    except IOError:
        print(f'Error: Unable to write to file {filename}.')

def main():
    log_filename = 'mission_computer_main.log'
    log_lines = read_log_file(log_filename)
    
    if log_lines:
        print('Log contents:')
        issues = analyze_log(log_lines)
        
        if issues:
            save_issues(issues, 'issues.log')
        
        
        report = '''# Log Analysis Report

## Overview
The log file contains information about the rocket launch mission. The mission seemed to be successful until the last stage.

## important events
1. Rocket initialization and pre-launch checks have been successfully completed.
2. The take-off and elevation phases went ahead as planned.
3. Satellite deployment was successful.
4. Rocket reentry and landing were successful early on.
5. After landing, there was a serious problem with the oxygen tank.

## a matter of importance
- At 11:35, the oxygen tank became unstable.
- At 11:40, the oxygen tank explosion occurred.

## Conclusion
Major mission objectives, including successful satellite deployment, have been achieved, but fatal failures have occurred after rocket landing. The instability of the oxygen tank leading to the explosion suggests that a serious malfunction occurred during the post-landing phase. This event requires immediate investigation to determine the root cause and prevent similar occurrences in future missions.

## Recommendation
1. Inspect the oxygen tank system thoroughly.
2. Review and strengthen safety protocols after landing.
3. Implement additional monitoring systems for critical components at all mission stages.
4. A comprehensive review of all systems identifies potential similar vulnerabilities.
'''
        
        try:
            with open('log_analysis.md', 'w', encoding='utf-8') as file:
                file.write(report)
            print('Report saved to log_analysis.md')
        except IOError:
            print('Error: Unable to write report to log_analysis.md')

if __name__ == '__main__':
    main()